import json
import os
from src.modules.types import JobMetadata, Status
from src.modules.utils import (
    check_if_folder_exists,
    check_if_file_exists,
    create_folder,
)


def get_job_logs(
    directory: str = "./logs", file_name: str = "log_list.json"
) -> list[str]:
    """
    Returns a list of job log IDs that are available.
    """

    LOG_LIST_FILE = os.path.join(directory, file_name)

    if not check_if_folder_exists(directory):
        create_folder(directory)

    if not check_if_file_exists(LOG_LIST_FILE):
        with open(LOG_LIST_FILE, "w") as f:
            json.dump([], f, indent=4)

    with open(LOG_LIST_FILE, "r") as openfile:
        file_content = openfile.read().strip()
        logs = json.loads(file_content) if file_content else []

    log_ids = [log["id"] for log in logs]

    return log_ids


def write_job_log(id: str, metadata: JobMetadata, directory: str = "./logs") -> None:
    """
    Given a job log ID and metadata, serialize and store the metadata.
    """
    # TODO: Implement this function and clean up the mock data
    pass


def read_job_log(id: str, directory: str = "./logs") -> JobMetadata:
    """
    Given a job log ID, read and deserialize the metadata.

    Returns the metadata for the given ID.

    Raises an exception if the log ID is not found.
    """
    # TODO: Implement this function and clean up the mock data
    return JobMetadata(
        id=id,
        status="success",
        repo_url="https://github.com/dd2480-spring-2025-group-1/assignment-1",
        ref="main",
        head_commit="b7f1a1c",
        author="Strengthless",
        time_started="2025-03-25T12:00:00Z",
        time_ended="2025-03-25T12:30:00Z",
        logs=["Mocked log 1", "Mocked log 2", "Mocked log 3", "Mocked log 4"],
    )
