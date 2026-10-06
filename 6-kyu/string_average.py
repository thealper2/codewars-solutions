import math

def average_string(s):
    nums = {
        'zero': 0, 'one': 1, 'two': 2,
        'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9
    }
    total = 0
    n = 0
    
    for word in s.split():
        value = nums.get(word, -1)
        if value >= 0:
            total += value
            n += 1
        else:
            return 'n/a'

    if n == 0:
        return 'n/a'

    result = [k for k, v in nums.items() if v == math.floor(total / n)]
    return result[0]