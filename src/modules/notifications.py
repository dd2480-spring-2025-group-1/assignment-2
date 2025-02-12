from src.modules.types import Status
from fastapi import HTTPException
import requests
import os


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
    url = f"https://api.github.com/repos/{owner}/{repo}/statuses/{sha}"

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN is not set.")

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    payload = {
        "state": state.value,
        "description": f"Custom CI/CD job {id} is {state.value}.",
        "context": "custom-ci/lint-and-test",
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 201:
        raise HTTPException(
            status_code=response.status_code, detail="Failed to update commit status."
        )


def get_commit_status(owner: str, repo: str, ref: str) -> Status:
    """
    Get the latest commit status for a given repository and commit reference.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :param repo: The name of the repository without the `.git` extension. The name is not case sensitive.
    :param ref: The commit reference. Can be a commit SHA, branch name (`heads/BRANCH_NAME`), or tag name (`tags/TAG_NAME`). For more information, see "Git References" in the Git documentation.
    """

    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{ref}/status"

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN is not set.")

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Failed to get commit status."
        )

    return response.json()
