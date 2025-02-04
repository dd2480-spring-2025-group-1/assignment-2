import logging
import time
import uvicorn
from typing import Union
from uuid import uuid4
from fastapi import FastAPI, BackgroundTasks, status, Response
from src.modules.actions import (
    checkout_ref,
    clone_repo,
    run_linter_check,
    run_tests,
    setup_dependencies,
)
from src.modules.logs import get_job_logs, read_job_log, write_job_log
from src.modules.notifications import add_commit_status
from src.modules.types import (
    HealthCheckResponse,
    JobMetadata,
    LogNotFoundResponse,
    LogsResponse,
    PushEventPayload,
    Status,
    WebhookResponse,
)
from src.modules.utils import create_folder, remove_folder


app = FastAPI(
    title="CI/CD Service API for DD2480",
    description="This API is used to interact with the custom CI/CD service for DD2480 assignment 2.",
    version="0.1.0",
    contact={
        "name": "Group 1",
        "url": "https://kth.name",
        "email": "thkam@kth.se",
    },
)
logging.basicConfig(level=logging.INFO)


@app.get("/")
def health_check() -> HealthCheckResponse:
    """
    This is the root path of the API.

    It indicates that the server is running, and returns a welcome message.
    """
    return {
        "health": "ok",
        "message": "Please navigate to `/redoc` to see the API documentation.",
    }


def ci_check(payload: PushEventPayload) -> None:
    """
    This function is used to run the CI checks on the incoming payload.
    """
    # Skip CI checks in special cases:
    # If a branch is created, but no commits are pushed.
    if payload.created and payload.commits == []:
        return

    # Create a unique ID for the job
    uuid = str(uuid4())
    status = Status.PENDING
    time_started = int(time.time())
    logs: list[str] = []

    try:
        logging.info(f"[{uuid}] Starting CI check...")
        # Extract some information from the payload
        repo_owner = payload.repository["owner"]["login"]
        repo_name = payload.repository["name"]
        clone_url = payload.repository["clone_url"]
        commit_sha = payload.after
        author = payload.pusher.name
        ref = payload.ref

        # Post a pending status to the commit
        logging.info(f"[{uuid}] Posting a pending status to commit {commit_sha}...")
        add_commit_status(repo_owner, repo_name, commit_sha, status, uuid)

        # Initialize an ephemeral environment
        ephemeral_folder = f"./temp/{uuid}/"
        create_folder(ephemeral_folder)

        # Begin setting up the CI environment
        logging.info(f"[{uuid}] Cloning the repository {repo_name}...")
        logs += [clone_repo(clone_url, ephemeral_folder)]
        repo_folder = ephemeral_folder + repo_name

        logging.info(f"[{uuid}] Checking out the commit {commit_sha}...")
        logs += [checkout_ref(repo_folder, commit_sha)]

        logging.info(f"[{uuid}] Setting up the dependencies...")
        logs += [setup_dependencies(repo_folder)]

        # Run the linter and tests
        logging.info(f"[{uuid}] Running the linter and tests...")
        linter_passed, log_4 = run_linter_check(repo_folder)
        logs += [log_4]

        tests_passed, log_5 = run_tests(repo_folder)
        logs += [log_5]

        # Update the status based on the CI checks
        status = Status.SUCCESS if linter_passed and tests_passed else Status.FAILURE

    except Exception as e:
        # Log the error and update the status
        logging.error(f"[{uuid}] An error occurred during the CI check: {e}")
        status = Status.ERROR

    finally:
        # Clean up the ephemeral environment
        remove_folder(ephemeral_folder)

        # Create the job metadata and store it as a log
        logging.info(f"[{uuid}] CI check completed with status {status}.")
        time_ended = int(time.time())
        job_metadata = JobMetadata(
            id=uuid,
            status=status,
            repo_url=clone_url,
            ref=ref,
            head_commit=commit_sha,
            author=author,
            time_started=time_started,
            time_ended=time_ended,
            logs=logs,
        )
        write_job_log(uuid, job_metadata)

        # Post the final status to the commit
        logging.info(f"[{uuid}] Posting the final status to commit {commit_sha}...")
        add_commit_status(repo_owner, repo_name, commit_sha, status, uuid)


@app.post("/webhook", status_code=status.HTTP_202_ACCEPTED)
def parse_incoming_webhook(
    payload: PushEventPayload, background_tasks: BackgroundTasks
) -> WebhookResponse:
    """
    This endpoint is used to receive and parse incoming webhooks.

    We currently only accept `push` events from GitHub.
    """
    background_tasks.add_task(ci_check, payload)
    return {
        "success": True,
        "message": "Webhook received successfully, the payload has been queued for processing.",
    }


@app.get("/logs")
def get_ci_logs() -> LogsResponse:
    """
    Returns a list of IDs for the logs that are available.

    Job logs are only stored after the CI job has been completed.
    """
    logs = get_job_logs()
    return {"logs": logs}


@app.get(
    "/logs/{id}",
    response_model=JobMetadata,
    responses={404: {"model": LogNotFoundResponse}},
)
def get_ci_log_details(
    id: str, response: Response
) -> Union[JobMetadata, LogNotFoundResponse]:
    """
    Returns the log details for the given ID.
    """
    try:
        job_metadata = read_job_log(id)
        return job_metadata
    except Exception:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": "Log not found. Either the log ID is invalid, or the CI job has not yet completed."
        }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
