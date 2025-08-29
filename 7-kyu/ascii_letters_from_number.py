def convert(number):
    n = len(number)
    result = ''
    for i in range(0, n - 1, 2):
        num = int(number[i:i+2])
        result += chr(num)
        
    return result
