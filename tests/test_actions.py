import unittest
from src.modules.actions import run_linter_check
from src.modules.utils import (
    write_to_file,
)


class ActionsTest(unittest.TestCase):

    # Tests for run_linter_check
    def test_linting_without_errors(self):
        ephermal_folder = "./temp/actions_test/"
        write_to_file(ephermal_folder + "hello.py", "print('hello world!')\n\n")
        output = run_linter_check(ephermal_folder)
        self.assertTrue(output[0])

    def test_linting_with_errors(self):
        ephermal_folder = "./temp/actions_test/"
        write_to_file(ephermal_folder + "hello.py", "print('hello world!)")
        output = run_linter_check(ephermal_folder)
        self.assertFalse(output[0])
        self.assertTrue("E999 SyntaxError" in output[1])
