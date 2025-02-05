from enum import Enum
from pydantic import BaseModel, Field


class Author(BaseModel):
    date: str | None = None
    email: str | None = None
    name: str = Field(description="The git author's name.")
    username: str | None = None


class Commit(BaseModel):
    added: list[str] | None = (
        Field(
            default=None,
            description="An array of files added in the commit. A maximum of 3000 changed files will be reported per commit.",
        ),
    )
    author: Author = Field(
        description="Metaproperties for Git author/committer information.",
    )
    committer: Author = Field(
        description="Metaproperties for Git author/committer information.",
    )
    distinct: bool = Field(
        description="Whether this commit is distinct from any that have been pushed before.",
    )
    id: str
    message: str = Field(
        description="The commit message.",
    )
    modified: list[str] | None = Field(
        description="An array of files modified by the commit. A maximum of 3000 changed files will be reported per commit.",
    )
    removed: list[str] | None = Field(
        description="An array of files removed in the commit. A maximum of 3000 changed files will be reported per commit.",
    )
    timestamp: str = Field(
        description="The ISO 8601 timestamp of the commit.",
    )
    tree_id: str
    url: str = Field(
        description="URL that points to the commit API resource.",
    )


class PushEventPayload(BaseModel):
    after: str = Field(
        description="The SHA of the most recent commit on `ref` after the push."
    )
    base_ref: str | None = None
    before: str = Field(
        description="The SHA of the most recent commit on `ref` before the push."
    )
    commits: list[Commit] = Field(
        description="An array of commit objects describing the pushed commits. (Pushed commits are all commits that are included in the `compare` between the `before` commit and the `after` commit.) The array includes a maximum of 2048 commits. If necessary, you can use the Commits API to fetch additional commits."
    )
    compare: str = Field(
        description="URL that shows the changes in this `ref` update, from the `before` commit to the `after` commit. For a newly created `ref` that is directly based on the default branch, this is the comparison between the head of the default branch and the `after` commit. Otherwise, this shows all commits until the `after` commit."
    )
    created: bool = Field(description="Whether this push created the `ref`.")
    deleted: bool = Field(description="Whether this push deleted the `ref`.")
    enterprise: dict | None = Field(
        default=None,
        description='An enterprise on GitHub. Webhook payloads contain the enterprise property when the webhook is configured on an enterprise account or an organization that\'s part of an enterprise account. For more information, see "About enterprise accounts."',
    )
    forced: bool = Field(
        description="Whether this push was a force push of the `ref`.",
    )
    head_commit: Commit | None = None
    installation: dict | None = Field(
        default=None,
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured for and sent to a GitHub App. For more information, see "Using webhooks with GitHub Apps."',
    )
    organization: dict | None = Field(
        default=None,
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an organization, or when the event occurs from activity in a repository owned by an organization.",
    )
    pusher: Author = Field(
        description="Metaproperties for Git author/committer information.",
    )
    ref: str = Field(
        description="The full git ref that was pushed. Example: `refs/heads/main` or `refs/tags/v3.14.1`."
    )
    repository: dict = Field(description="A git repository")
    sender: dict = Field(description="A GitHub user.")


class HealthCheckResponse(BaseModel):
    health: str = "ok"
    message: str = "Please navigate to `/redoc` to see the API documentation."


class WebhookResponse(BaseModel):
    success: bool = True
    message: str = (
        "Webhook received successfully, the payload has been queued for processing."
    )


class LogsResponse(BaseModel):
    logs: list[str] = Field(
        description="A list of IDs for the logs that are available."
    )


class LogNotFoundResponse(BaseModel):
    message: str = (
        "Log not found. Either the log ID is invalid, or the CI job has not yet completed."
    )


class Status(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    PENDING = "pending"
    ERROR = "error"


class JobMetadata(BaseModel):
    id: str
    status: Status

    repo_url: str
    ref: str
    head_commit: str = Field(
        description="The SHA of the most recent commit on `ref` after the push."
    )
    author: str

    time_started: int
    time_ended: int

    logs: list[str] = Field(
        description="The CLI logs for the job, split into four sections: `clone`, `setup`, `lint`, `test`."
    )
