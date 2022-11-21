import unittest

from grains import square, total


class GrainsTest(unittest.TestCase):
    def test_square_1(self):
        self.assertEqual(1, square(1))

    def test_square_2(self):
        self.assertEqual(2, square(2))

    def test_square_3(self):
        self.assertEqual(4, square(3))

    def test_square_4(self):
        self.assertEqual(8, square(4))

    def test_square_16(self):
        self.assertEqual(32768, square(16))

    def test_square_32(self):
        self.assertEqual(2147483648, square(32))

    def test_square_64(self):
        self.assertEqual(9223372036854775808, square(64))
        self.assertEqual(18446744073709551615, total())


if __name__ == '__main__':
    unittest.main()
