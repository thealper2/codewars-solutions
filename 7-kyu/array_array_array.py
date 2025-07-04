def explode(arr):
    a, b = arr
    if type(a) != int and type(b) != int:
        return "Void!"
    if type(a) == int and type(b) == int:
        return [arr] * (a + b)
    if type(a) == int:
        return [arr] * a
    else:
        return [arr] * b
