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
    log_list_file = os.path.join(directory, "log_list.json")

    if not check_if_folder_exists(directory):
        create_folder(directory)

    if not check_if_file_exists(log_list_file):
        with open(log_list_file, "w") as f:
            json.dump([], f, indent=4)

    with open(log_list_file, "r") as openfile:
        file_content = openfile.read().strip()
        log_ids = json.loads(file_content) if file_content else []

    return log_ids


def write_job_log(
    id: str,
    metadata: JobMetadata,
    directory: str = "./logs",
) -> None:
    """
    Given a job log ID and metadata, serialize and store the metadata.
    """
    log_list_file = os.path.join(directory, "log_list.json")
    log_file = os.path.join(directory, f"{id}.json")

    if not check_if_folder_exists(directory):
        create_folder(directory)

    with open(log_file, "w") as outfile:
        json.dump(metadata.model_dump(mode="json"), outfile, indent=4)

    if not check_if_file_exists(log_list_file):
        log_ids = []
    else:
        with open(log_list_file, "r") as openfile:
            file_content = openfile.read().strip()
            log_ids = json.loads(file_content) if file_content else []

    if id not in log_ids:
        log_ids.append(id)
        with open(log_list_file, "w") as outfile:
            json.dump(log_ids, outfile, indent=4)
    pass


def read_job_log(id: str, directory: str = "./logs") -> JobMetadata:
    """
    Given a job log ID, read and deserialize the metadata.

    Returns the metadata for the given ID.

    Raises an exception if the log ID is not found.
    """
    log_file = os.path.join(directory, f"{id}.json")

    if not check_if_file_exists(log_file):
        raise ValueError(f"Log ID {id} not found.")

    with open(log_file, "r") as openfile:
        file_content = openfile.read().strip()
        log_data = json.loads(file_content) if file_content else {}

    return JobMetadata(**log_data)
