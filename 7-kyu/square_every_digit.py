def square_digits(num):
    if num == 0:
        return 0
    
    result = ""
    for digit in str(num):
        squared = int(digit) ** 2
        result += str(squared)
        
    return int(result)