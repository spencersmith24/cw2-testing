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

    def test_to_roman_cache(self):
        # we can access private variables like this
        # private variables aren't really "private" like they are in java
        # they're what's called "mangled," which means we can access them
        # with a more convoluted name, but we're not supposed to
        # however, it is useful for testing purposes
        self.converter._RomanNumeralConverter__arabic_to_roman_cache[1] = "test value"
        self.assertEqual("test value", self.converter.to_roman(1))
        # here, we assert that it doesn't convert the value anew, and rather
        # sees that the value is in the cache, and just returns that

if __name__ == '__main__': main()
