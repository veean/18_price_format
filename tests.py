import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_solves_real_roots(self):
        beautiful_price = format_price(1)
        self.assertEqual(beautiful_price, 1)

    def test_negative_price(self):
        beautiful_price = format_price(-56.01)
        self.assertEqual(beautiful_price, None)

    def test_second_root_is_none_if_one_solution(self):
        beautiful_price = format_price(1)
        self.assertIsNotNone(beautiful_price, 1)

    def test_returns_none_for_complex_solution(self):
        beautiful_price = format_price(1)
        self.assertIsNone(beautiful_price, 1)


if __name__ == '__main__':
    unittest.main()

