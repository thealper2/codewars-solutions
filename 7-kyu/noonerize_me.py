def noonerize(numbers):
    if type(numbers[0]) != int or type(numbers[1]) != int:
        return "invalid array"
    
    a, b = map(str, numbers)
    return abs(int(b[0] + a[1:]) - int(a[0] + b[1:]))
