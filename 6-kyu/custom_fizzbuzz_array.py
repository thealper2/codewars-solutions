def fizz_buzz_custom(string_one='Fizz', string_two='Buzz', num_one=3, num_two=5): 
    result = []
    for i in range(1, 101):
        word = ''
        if i % num_one == 0:
            word += string_one
        if i % num_two == 0:
            word += string_two
        result.append(word if word else i)
        
    return result