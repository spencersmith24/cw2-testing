class RomanNumeralConverter:

    def __init__(self) -> None:
        self.__roman_to_arabic_cache = {}
        self.__arabic_to_roman_cache = {}

    def __getitem__(self, item):
        if type(item) is str:
            return self.from_roman(item)
        elif type(item) is int:
            return self.to_roman(item)
        else: raise ValueError("Cannot subscript RomanNumeralConverter with '%s', expected 'str' or 'int'"%type(item))

    def from_roman(self, roman_number: int):
        roman_numeral = roman_number.lower()
        if roman_numeral in self.__roman_to_arabic_cache.keys():
            return self.__roman_to_arabic_cache[roman_numeral]
        return_value = 0
        for index,character in enumerate(roman_numeral):
            match character:
                case 'i':
                    try: return_value+=4 if roman_numeral[index+1] == 'v' else 9 if roman_numeral[index+1]=='x' else 1
                    except IndexError: return_value += 1
                    else: continue
                case 'v':
                    try:
                        if roman_numeral[index-1]=='i'and index-1>=0:continue
                    except IndexError:pass
                    return_value+=5
                case 'x':
                    try:
                        if roman_numeral[index-1]=='i'and index-1>=0:continue
                    except IndexError:pass
                    try:return_value+=40 if roman_numeral[index+1]=='l' else 90 if roman_numeral[index+1] == 'c' else 10
                    except IndexError: return_value+=10
                case 'l':
                    try:
                        if roman_numeral[index-1]=='x'and index-1>=0:continue
                    except IndexError:pass
                    return_value+=50
                case 'c':
                    try:
                        if roman_numeral[index-1]=='x'and index-1>=0:continue
                    except IndexError:pass
                    try:return_value+=400 if roman_numeral[index+1]=='d'else 900 if roman_numeral[index+1]=='m'else 100
                    except IndexError:return_value+=100
                case 'd':
                    try:
                        if roman_numeral[index-1]=='c'and index-1>=0:continue
                    except IndexError:pass
                    return_value+=500
                case 'm':
                    try:
                        if roman_numeral[index-1]=='c'and index-1>=0:continue
                    except IndexError:pass
                    return_value+=1000
                case _: raise ValueError("only numerals IVXLCDM are supported")
        self.__roman_to_arabic_cache[roman_numeral] = return_value
        return return_value
    def to_roman(self, arabic_number: int):
        if type(arabic_number) is not int:
            raise TypeError("Expected type int, got %s"%str(type(arabic_number)))
        if arabic_number in self.__arabic_to_roman_cache.keys():
            return self.__arabic_to_roman_cache[arabic_number]
        if arabic_number<4000:
            if arabic_number>0:
                return_value=str()
                return_value+=('', 'M', 'MM', 'MMM')[arabic_number//1000]if arabic_number>999 else str()
                return_value+=('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')[int((arabic_number//100).__str__()[-1])]if arabic_number>99 else str()
                return_value+=('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')[int((arabic_number//10).__str__()[-1])]if arabic_number>9 else str()
                return_value+=('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')[int(arabic_number.__str__()[-1])]
                self.__arabic_to_roman_cache[arabic_number] = return_value
                return return_value
            else:raise ValueError("only positive numbers are supported")
        else:raise ValueError("only numbers up to 3999 are supported")

if __name__ == "__main__":
    converter = RomanNumeralConverter()
    while True:
        number = input("Input a number to convert or ‘q’ to quit\n>> ")
        if number == 'q': break
        try: print(converter[int(number)])
        except ValueError: print(converter[number])