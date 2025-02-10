import unittest
import os
import json
from src.modules.logs import get_job_logs, write_job_log, read_job_log
from src.modules.utils import check_if_folder_exists, remove_folder
from src.modules.types import JobMetadata


class TestUtils(unittest.TestCase):
    # Set up the test environment
    def setUp(self):
        self.ephemeral_folder = "./temp/log_test/"
        self.ephemeral_file = os.path.join(self.ephemeral_folder, "log_list.json")

        os.makedirs(self.ephemeral_folder, exist_ok=True)

    def tearDown(self):
        if check_if_folder_exists(self.ephemeral_folder):
            remove_folder(self.ephemeral_folder)

    def mock_data(self, id: str):
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
        mock1 = self.mock_data("ad21")
        mock2 = self.mock_data("df44")

        logs = []

        logs.append(mock1.model_dump(mode="json"))
        logs.append(mock2.model_dump(mode="json"))

        with open(self.ephemeral_file, "w") as outfile:
            json.dump(logs, outfile, indent=4)

        result = get_job_logs(self.ephemeral_folder)

        self.assertIn("ad21", result)
        self.assertIn("df44", result)
        self.assertEqual(len(result), 2)

    def test_get_job_log(self):
        mock = self.mock_data("ad21")

        logs = []

        logs.append(mock.model_dump(mode="json"))

        with open(self.ephemeral_file, "w") as outfile:
            json.dump(logs, outfile, indent=4)

        result = get_job_logs(self.ephemeral_folder)

        self.assertIn("ad21", result)
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
