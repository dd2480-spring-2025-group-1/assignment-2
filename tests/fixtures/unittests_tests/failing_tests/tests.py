import unittest

# All these tests fail
class TestTests(unittest.TestCase):
    def test_this_should_fail_to_be_true(self):
        self.assertTrue(False)

    def test_this_should_fail_to_be_false(self):
        self.assertFalse(True)

    def test_string__does_not_contain_substring(self):
        self.assertIn("substrings", "this string contains a substring")

if __name__ == "__main__":
    unittest.main()
