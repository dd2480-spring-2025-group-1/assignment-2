import unittest
from src.modules.actions import (
    checkout_ref,
    clone_repo,
    setup_dependencies,
    run_linter_check,
    run_tests,
)
from src.modules.utils import (
    check_if_file_exists,
    check_if_folder_exists,
    remove_folder,
)


class ActionsTest(unittest.TestCase):
    # Set up the test environment
    def setUp(self):
        self.target_repo = (
            "https://github.com/dd2480-spring-2025-group-1/assignment-1.git"
        )
        self.ephemeral_folder = "./temp/actions_test/"
        self.repo_folder = self.ephemeral_folder + "assignment-1/"

    def tearDown(self):
        if check_if_folder_exists(self.ephemeral_folder):
            remove_folder(self.ephemeral_folder)

    # Tests for clone_repo
    def test_clone_repo_successfully(self):
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))

        clone_repo(self.target_repo, self.ephemeral_folder)

        does_repo_exist = check_if_folder_exists(self.repo_folder)
        self.assertTrue(does_repo_exist)

    def test_clone_repo_failure(self):
        with self.assertRaises(Exception):
            clone_repo("https://guthib.com", self.ephemeral_folder)

    # Tests for checkout_ref
    def test_checkout_ref_successfully(self):
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))

        clone_repo(self.target_repo, self.ephemeral_folder)
        checkout_ref(self.repo_folder, "origin/do-not-delete-for-tests")

        self.assertTrue(
            check_if_file_exists(self.repo_folder + "feature_file_after_checkout.txt")
        )

    def test_checkout_ref_failure(self):
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))

        clone_repo(self.target_repo, self.ephemeral_folder)

        with self.assertRaises(Exception):
            checkout_ref(self.repo_folder, "origin/non_existent_ref")

    # Tests for setup_dependencies
    def test_setup_dependencies_successfully(self):
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))

        clone_repo(self.target_repo, self.ephemeral_folder)
        setup_dependencies(self.ephemeral_folder + "assignment-1")

        does_venv_exist = check_if_folder_exists(
            self.ephemeral_folder + "assignment-1/.venv"
        )
        self.assertTrue(does_venv_exist)

    def test_setup_dependencies_failure(self):
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))

        with self.assertRaises(Exception):
            setup_dependencies(self.ephemeral_folder + "assignment-1")

    # Tests for run_linter_check
    def test_linting_without_errors(self):
        check, _ = run_linter_check("tests/fixtures/flake8_tests/syntax_correct")
        self.assertTrue(check)

    def test_linting_with_E9_errors(self):
        check, logs = run_linter_check("tests/fixtures/flake8_tests/trigger_E9")
        self.assertFalse(check)
        self.assertTrue("E9" in logs)

    def test_linting_with_F7_errors(self):
        check, logs = run_linter_check("tests/fixtures/flake8_tests/trigger_F7")
        self.assertFalse(check)
        self.assertTrue("F7" in logs)

    def test_linting_with_F63_errors(self):
        check, logs = run_linter_check("tests/fixtures/flake8_tests/trigger_F63")
        self.assertFalse(check)
        self.assertTrue("F631" in logs)
        self.assertTrue("F632" in logs)

    def test_linting_with_F82_errors(self):
        check, logs = run_linter_check("tests/fixtures/flake8_tests/trigger_F82")
        self.assertFalse(check)
        self.assertTrue("F82" in logs)

    # Tests for run_tests
    def test_run_sucessful_tests(self):
        check, logs = run_tests("tests/fixtures/unittests_tests/successful_tests")
        self.assertTrue(check)
        self.assertTrue("OK" in logs)

    def test_run_failing_tests(self):
        check, logs = run_tests("tests/fixtures/unittests_tests/failing_tests")
        self.assertFalse(check)
        self.assertTrue("FAILED" in logs)


if __name__ == "__main__":
    unittest.main()
