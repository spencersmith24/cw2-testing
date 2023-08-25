## `from_roman(roman_number: str) -> int`:

### Raises:
- 'TypeError', when aregument passed is not of type 'str'
- 'ValueError', when argument passed contains numeral that is not '"IVXLCDMivxlcdm"'

> This method takes in a parameter containing a Roman numeral (from I to M) and converts it into an integer. For example, if passed `"I"`, it'll return `1`, and if passed `"lxxiii"`, it will return 73 (L := 50 + X := 10 + X + I := 1 + I + I).