import json
import os
from src.modules.types import JobMetadata, Status
from src.modules.utils import (
    check_if_folder_exists,
    check_if_file_exists,
    create_folder,
)


def get_job_logs(
    directory: str = "./logs",
) -> list[str]:
    """
    Returns a list of job log IDs that are available.
    """
    file_name = "log_list.json"

    log_list_file = os.path.join(directory, file_name)

    if not check_if_folder_exists(directory):
        create_folder(directory)

    if not check_if_file_exists(log_list_file):
        with open(log_list_file, "w") as f:
            json.dump([], f, indent=4)

    with open(log_list_file, "r") as openfile:
        file_content = openfile.read().strip()
        logs = json.loads(file_content) if file_content else []

    log_ids = [log["id"] for log in logs]

    return log_ids


def write_job_log(
    id: str,
    metadata: JobMetadata,
    directory: str = "./logs",
) -> None:
    """
    Given a job log ID and metadata, serialize and store the metadata.
    """
    file_name = "log_list.json"

    log_list_file = os.path.join(directory, file_name)

    if not check_if_folder_exists(directory):
        create_folder(directory)

    if not check_if_file_exists(log_list_file):
        logs = []
    else:
        with open(log_list_file, "r") as openfile:
            file_content = openfile.read().strip()
            logs = json.loads(file_content) if file_content else []

    logs.append(metadata.model_dump(mode="json"))

    with open(log_list_file, "w") as outfile:
        json.dump(logs, outfile, indent=4)
    pass


def read_job_log(id: str, directory: str = "./logs") -> JobMetadata:
    """
    Given a job log ID, read and deserialize the metadata.

    Returns the metadata for the given ID.

    Raises an exception if the log ID is not found.
    """
    file_name = "log_list.json"

    log_list_file = os.path.join(directory, file_name)

    if not check_if_folder_exists(directory):
        create_folder(directory)

    if not check_if_file_exists(log_list_file):
        with open(log_list_file, "w") as f:
            json.dump([], f, indent=4)

    with open(log_list_file, "r") as openfile:
        file_content = openfile.read().strip()
        logs = json.loads(file_content) if file_content else []

    for log in logs:
        if log["id"] == id:
            return JobMetadata(
                id=log["id"],
                status=log["status"],
                repo_url=log["repo_url"],
                ref=log["ref"],
                head_commit=log["head_commit"],
                author=log["author"],
                time_started=log["time_started"],
                time_ended=log["time_ended"],
                logs=log["logs"],
            )
    raise Exception(f"Log ID {id} not found.")
