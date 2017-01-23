import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_integer_values(self):
        beautiful_price = format_price(3245)
        self.assertEqual(beautiful_price, '3 245')

    def test_float_values(self):
        beautiful_price = format_price(3245.42342)
        self.assertIsNotNone(beautiful_price, '3 245.42')

    def test_negative_price(self):
        beautiful_price = format_price(-56.01)
        self.assertEqual(beautiful_price, None)

    def test_integer_with_nulls(self):
        beautiful_price = format_price('446,000000')
        self.assertEqual(beautiful_price, '446')

    def test_incorrect_type_values(self):
        beautiful_price_one = format_price([587.6])
        beautiful_price_two = format_price((123213, 3213))
        beautiful_price_three = format_price({'abc'})
        self.assertEqual((beautiful_price_one, beautiful_price_two, beautiful_price_three), (None, None, None))

if __name__ == '__main__':
    unittest.main()
