import unittest
from unittest.mock import patch, MagicMock
import os
from src.modules.notifications import add_commit_status, get_commit_status
from src.modules.types import Status


class TestNotification(unittest.TestCase):

    def mock_test_add_commit_status_failure(self):
        owner = "test_owner"
        repo = "test_repo"
        sha = "test_sha"
        state = Status.FAILURE
        id = "test_id"

        with patch("requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 400
            mock_post.return_value = mock_response

            with patch.dict(os.environ, {"GITHUB_TOKEN": "fake-token"}):
                with self.assertRaises(Exception):
                    add_commit_status(owner, repo, sha, state, id)

    def test_add_commit_status_success(self):
        owner = "dd2480-spring-2025-group-1"
        repo = "assignment-2"
        sha = "05f31566c2bf5c335c2ef11380d42615b812879f"
        state = Status.SUCCESS
        id = "test_id"

        add_commit_status(owner, repo, sha, state, id)

        status = get_commit_status(owner, repo, sha)

        self.assertEqual(status, "success", "Commit status did not update to sucess")

    def test_add_commit_status_failurei(self):
        owner = "dd2480-spring-2025-group-1"
        repo = "assignment-2"
        sha = "05f31566c2bf5c335c2ef11380d42615b812879f"
        state = Status.FAILURE
        id = "test_id"

        add_commit_status(owner, repo, sha, state, id)

        status = get_commit_status(owner, repo, sha)

        self.assertEqual(status, "failure", "Commit status did not update to failure")

    def test_value_error_missing_token(self):
        owner = "test_owner"
        repo = "test_repo"
        sha = "test_sha"
        state = Status.FAILURE
        id = "test_id"

        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError) as context:
                add_commit_status(owner, repo, sha, state, id)

            self.assertEqual(str(context.exception), "GITHUB_TOKEN is not set.")


if __name__ == "__main__":
    unittest.main()
