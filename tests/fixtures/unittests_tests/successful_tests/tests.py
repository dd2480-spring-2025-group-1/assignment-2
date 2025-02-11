import unittest

# All these tests succeed
class TestTests(unittest.TestCase):
    def test_this_should_be_true(self):
        self.assertTrue(True)

    def test_string_contains_substring(self):
        self.assertIn("substring", "this string contains a substring")

if __name__ == "__main__":
    unittest.main()
