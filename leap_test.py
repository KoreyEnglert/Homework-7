import unittest
import leap

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(leap.is_leap(1), False);

    def test_add2(self):
        self.assertEqual(leap.is_leap(4), True);

    def test_add3(self):
        self.assertEqual(leap.is_leap(100), False);

    def test_add4(self):
        self.assertEqual(leap.is_leap(400), True);
if __name__ == '__main__':
    unittest.main()
