from snapshottest import TestCase
import unittest


class TestUtils(TestCase):
    def test_add(self):
        self.assertMatchSnapshot(1 + 1)


if __name__ == "__main__":
    unittest.main()
