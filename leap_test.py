import unittest
import leap

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(leap.is_leap(1), False);

if __name__ == '__main__':
    unittest.main()
