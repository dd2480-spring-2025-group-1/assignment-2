import unittest
import os
import json
from src.modules.logs import get_job_logs, write_job_log, read_job_log
from src.modules.utils import check_if_folder_exists, remove_folder
from src.modules.types import JobMetadata


class TestUtils(unittest.TestCase):
    # Set up the test environment
    def setUp(self):
        self.fixture_folder = "tests/fixtures/log_tests/get_job_logs"

    # Tests for get_job_logs
    def test_get_job_logs(self):
        result = get_job_logs(self.fixture_folder, "multiple_log.json")

        self.assertIn("ad21", result)
        self.assertIn("df44", result)
        self.assertEqual(len(result), 2)

    def test_get_job_log(self):
        result = get_job_logs(self.fixture_folder, "single_log.json")

        self.assertIn("ad21", result)
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
