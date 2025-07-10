def convert_palindromes(numbers):
    return [1 if str(number) == str(number)[::-1] else 0 for number in numbers ]
