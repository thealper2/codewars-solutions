class RomanNumerals:
    @staticmethod
    def to_roman(num : int) -> str:
        roman = {
            1: 'I', 4: 'IV', 5: 'V',
            9: 'IX', 10: 'X', 40: 'XL',
            50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM',
            1000: 'M',
        }
        result = ''
        for value, symbol in sorted(roman.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value

        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman_values = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000
        }
        result = 0
        prev_value = 0

        for c in roman_num:
            value = roman_values[c]
            result += value
            if value > prev_value:
                result -= 2 * prev_value

            prev_value = value

        return result