from unittest import TestCase, main
from clean_code import RomanNumeralConverter


class TestRomanNumeralConverter(TestCase):
    def setUp(self):
        self.converter = RomanNumeralConverter()

    def tearDown(self):
        del self.converter
    
    def test_to_roman_conversion(self):
        self.assertEqual(self.converter.to_roman(578), "DLXXVIII")
    
    def test_to_roman_negative(self):
        with self.assertRaises(ValueError):
            self.converter.to_roman(-1)
    
    def test_to_roman_out_of_range(self):
        with self.assertRaises(ValueError):
            self.converter.to_roman(4000)


if __name__ == '__main__': main()
