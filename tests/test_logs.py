import unittest
import os
import json
from src.modules.logs import get_job_logs, write_job_log, read_job_log
from src.modules.utils import check_if_folder_exists, remove_folder
from src.modules.types import JobMetadata
from typing import Optional, List


class TestUtils(unittest.TestCase):
    # Set up the test environment
    def setUp(self):
        self.fixture_folder = "tests/fixtures/log_tests"
        self.ephemeral_folder = "./temp/log_test/"

    def tearDown(self):
        if check_if_folder_exists(self.ephemeral_folder):
            remove_folder(self.ephemeral_folder)

    # Function for creating mock JobMetadata
    def mock_metadata(
        self,
        id: str,
        status: Optional[str] = "success",
        repo_url: Optional[
            str
        ] = "https://github.com/dd2480-spring-2025-group-1/assignment-1",
        ref: Optional[str] = "main",
        head_commit: Optional[str] = "b7f1a1c",
        author: Optional[str] = "Joel90689",
        time_started: Optional[int] = 21,
        time_ended: Optional[int] = 23,
        logs: Optional[List[str]] = [
            "Mocked log 1",
            "Mocked log 2",
            "Mocked log 3",
            "Mocked log 4",
        ],
    ) -> JobMetadata:
        return JobMetadata(
            id=id,
            status=status,
            repo_url=repo_url,
            ref=ref,
            head_commit=head_commit,
            author=author,
            time_started=time_started,
            time_ended=time_ended,
            logs=logs,
        )

    def test_get_job_logs(self):
        """
        Test getting multiple log ids and verifying what is returned.
        """
        result = get_job_logs(os.path.join(self.fixture_folder, "multiple_log"))

        self.assertIn("ad21", result)
        self.assertIn("df44", result)
        self.assertEqual(len(result), 2)

    def test_get_job_log(self):
        """
        Test getting a single log id and verifying what has been returned.
        """
        result = get_job_logs(os.path.join(self.fixture_folder, "single_log"))

        self.assertIn("ad21", result)
        self.assertEqual(len(result), 1)

    def test_write_job_logs(self):
        """
        Test writing multiple logs to a file and verifying they can be read via get_job_logs().
        """
        mock1 = self.mock_metadata("ad21")
        mock2 = self.mock_metadata("df44")

        write_job_log("ad21", mock1, self.ephemeral_folder)
        write_job_log("df44", mock2, self.ephemeral_folder)

        ids = get_job_logs(self.ephemeral_folder)
        self.assertIn("ad21", ids)
        self.assertIn("df44", ids)
        self.assertEqual(len(ids), 2, "Expected exactly 2 IDs in the log file.")

    def test_write_job_log(self):
        """
        Test writing a single log and verifying its contents via read_job_log().
        """
        mock = self.mock_metadata("ad21")

        write_job_log("ad21", mock, self.ephemeral_folder)

        ids = get_job_logs(self.ephemeral_folder)
        self.assertIn("ad21", ids)
        self.assertEqual(len(ids), 1, "Expected 1 ID in the log file.")

    def test_read_job_log_and_write_job_log(self):
        """
        Test writing logs and reading what was written.
        """
        mock1 = self.mock_metadata(
            "as54", logs=["Mocked log 54", "Mocked log 55", "Mocked log 56"]
        )
        mock2 = self.mock_metadata(
            "bd34", logs=["Mocked log 34", "Mocked log 35", "Mocked log 36"]
        )
        write_job_log("as54", mock1, self.ephemeral_folder)
        write_job_log("bd34", mock2, self.ephemeral_folder)

        result1 = read_job_log("as54", self.ephemeral_folder)
        result2 = read_job_log("bd34", self.ephemeral_folder)

        self.assertEqual(mock1, result1)
        self.assertEqual(mock2, result2)

    def test_read_job_log_raises_exception(self):
        """
        Tests that read_job_log raises an exeption if the id can not be found.
        """
        self.assertRaises(
            Exception,
            read_job_log,
            "xxxx",
            os.path.join(self.fixture_folder, "multiple_log"),
        )

    def test_read_job_logs_and_write_job_logs_and_get_job_logs(self):
        """
        Test writing logs and reading what was written and log listing.
        """
        mock1 = self.mock_metadata(
            "as54", logs=["Mocked log 54", "Mocked log 55", "Mocked log 56"]
        )
        mock2 = self.mock_metadata(
            "bd34", logs=["Mocked log 34", "Mocked log 35", "Mocked log 36"]
        )
        write_job_log("as54", mock1, self.ephemeral_folder)
        write_job_log("bd34", mock2, self.ephemeral_folder)

        result1 = read_job_log("as54", self.ephemeral_folder)
        result2 = read_job_log("bd34", self.ephemeral_folder)

        logResult = get_job_logs(self.ephemeral_folder)

        self.assertEqual(mock1, result1)
        self.assertEqual(mock2, result2)

        self.assertIn("as54", logResult)
        self.assertIn("bd34", logResult)
        self.assertEqual(len(logResult), 2)


if __name__ == "__main__":
    unittest.main()
