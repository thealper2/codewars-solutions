def count(a, t, x):
    result = 0
    for num in a:
        if x == 0:
            if num == t:
                result += 1
        else:
            if (num - t) % x == 0:
                result += 1
                
    return result
