import unittest
import os
import json
from src.modules.logs import get_job_logs, write_job_log, read_job_log
from src.modules.utils import check_if_folder_exists, remove_folder
from src.modules.types import JobMetadata


class TestUtils(unittest.TestCase):
    # Set up the test environment
    def setUp(self):
        self.fixture_folder = "tests/fixtures/log_tests"
        self.ephemeral_folder = "./temp/log_test/"

    def tearDown(self):
        if check_if_folder_exists(self.ephemeral_folder):
            remove_folder(self.ephemeral_folder)

    # Function for creating mock JobMetadata
    def mock_metadata(self, id: str) -> JobMetadata:
        return JobMetadata(
            id=id,
            status="success",
            repo_url="https://github.com/dd2480-spring-2025-group-1/assignment-1",
            ref="main",
            head_commit="b7f1a1c",
            author="Strengthless",
            time_started=23,
            time_ended=23,
            logs=["Mocked log 1", "Mocked log 2", "Mocked log 3", "Mocked log 4"],
        )

    # Tests for get_job_logs
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

    # Tests for write_job_logs
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


if __name__ == "__main__":
    unittest.main()
