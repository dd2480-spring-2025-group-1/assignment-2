import unittest
from src.modules.utils import (
    check_if_folder_exists,
    check_if_file_exists,
    create_folder,
    write_to_file,
    remove_folder,
    remove_file,
)


class TestUtils(unittest.TestCase):
    # Set up the test environment
    def setUp(self):
        self.ephemeral_folder = "./temp/utils_test/"
        self.ephemeral_folder_nested = "./temp/utils_test/nested/"

    def tearDown(self):
        if check_if_folder_exists(self.ephemeral_folder):
            remove_folder(self.ephemeral_folder)

    # Tests for check_if_folder_exists
    def test_check_if_folder_exists(self):
        self.assertTrue(check_if_folder_exists("./src"))

    def test_check_if_folder_does_not_exist(self):
        self.assertFalse(check_if_folder_exists("./non_existent_folder"))

    # Tests for check_if_file_exists
    def test_check_if_file_exists(self):
        self.assertTrue(check_if_file_exists("./src/modules/utils.py"))

    def test_check_if_file_does_not_exist(self):
        self.assertFalse(check_if_file_exists("./non_existent_file.py"))

    # Tests for create_folder
    def test_create_folder(self):
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))
        create_folder(self.ephemeral_folder)
        self.assertTrue(check_if_folder_exists(self.ephemeral_folder))

    def test_create_nested_folder(self):
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))
        create_folder(self.ephemeral_folder_nested)
        self.assertTrue(check_if_folder_exists(self.ephemeral_folder_nested))

    # Tests for write_to_file
    def test_write_new_file(self):
        file_path = self.ephemeral_folder + "test_file.txt"
        content = "Hello, world!"
        write_to_file(file_path, content)

        self.assertTrue(check_if_file_exists(file_path))

    def test_overwrite_file(self):
        file_path = self.ephemeral_folder + "test_file.txt"
        content = "Hello, world!"
        write_to_file(file_path, content)
        self.assertTrue(check_if_file_exists(file_path))

        new_content = "Goodbye, world!"
        write_to_file(file_path, new_content)

        with open(file_path, "r") as file:
            self.assertEqual(file.read(), new_content)

    # Tests for remove_folder
    def test_remove_folder(self):
        create_folder(self.ephemeral_folder)
        self.assertTrue(check_if_folder_exists(self.ephemeral_folder))

        remove_folder(self.ephemeral_folder)
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder))

    def test_remove_nested_folder(self):
        create_folder(self.ephemeral_folder_nested)
        self.assertTrue(check_if_folder_exists(self.ephemeral_folder_nested))

        remove_folder(self.ephemeral_folder)
        self.assertFalse(check_if_folder_exists(self.ephemeral_folder_nested))

    # Tests for remove_file
    def test_remove_file(self):
        file_path = self.ephemeral_folder + "test_file.txt"
        write_to_file(file_path, "Hello, world!")
        self.assertTrue(check_if_file_exists(file_path))

        remove_file(file_path)
        self.assertFalse(check_if_file_exists(file_path))

    def test_remove_non_existent_file(self):
        file_path = self.ephemeral_folder + "non_existent_file.txt"
        self.assertFalse(check_if_file_exists(file_path))

        remove_file(file_path)
        self.assertFalse(check_if_file_exists(file_path))

    def test_remove_path_instead_of_file(self):
        create_folder(self.ephemeral_folder)
        self.assertTrue(check_if_folder_exists(self.ephemeral_folder))

        remove_file(self.ephemeral_folder)
        self.assertTrue(check_if_folder_exists(self.ephemeral_folder))


if __name__ == "__main__":
    unittest.main()
