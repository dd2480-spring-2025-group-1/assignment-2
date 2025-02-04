from src.modules.types import Status


def add_commit_status(
    owner: str,
    repo: str,
    sha: str,
    state: Status,
    id: str,
) -> None:
    """
    Add a new commit status.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :param repo: The name of the repository without the `.git` extension. The name is not case sensitive.
    :param sha: The SHA of the commit.
    :param state: The state of the status. Can be one of `success`, `failure`, `pending`, or `error`.
    :param id: The unique ID of the job.
    """
    # TODO: Check how exactly this works... If we already sent a pending job status, how do we update it later?
    # Does github automatically update the status check if we send a new one with the same context?

    # TODO: Implement this function - For the API call, we should default the target_url to the `/logs/{job_id}` endpoint, and the context to `custom-ci/lint-and-test`.
    # For the description, I guess we can just write some elaborations based off the status enums, then refer the user to the target_url for details?
    pass


def get_commit_status(owner: str, repo: str, ref: str) -> Status:
    """
    Get the combined status check for a given repository and commit reference.

    Note that only the latest 30 status checks are taken into account.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :param repo: The name of the repository without the `.git` extension. The name is not case sensitive.
    :param ref: The commit reference. Can be a commit SHA, branch name (`heads/BRANCH_NAME`), or tag name (`tags/TAG_NAME`). For more information, see "Git References" in the Git documentation.
    """
    # TODO: Implement this function.
    pass
