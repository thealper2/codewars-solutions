def order_weight(strng):
    numbers = strng.split()
    numbers.sort(key=lambda x: (sum(int(d) for d in x), x))
    return ' '.join(numbers)