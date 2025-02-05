from src.modules.types import JobMetadata


def get_job_logs() -> list[str]:
    """
    Returns a list of job log IDs that are available.
    """
    # TODO: Implement this function and clean up the mock data
    return [
        "bd042fa6-4924-4c4e-b773-8783e3e58174",
        "fd5c084c-ff7c-4651-9a52-37096242d81c",
    ]


def write_job_log(id: str, metadata: JobMetadata) -> None:
    """
    Given a job log ID and metadata, serialize and store the metadata.
    """
    # TODO: Implement this function and clean up the mock data
    pass


def read_job_log(id: str) -> JobMetadata:
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
