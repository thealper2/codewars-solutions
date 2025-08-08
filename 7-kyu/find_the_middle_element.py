def gimme(input_array):
    s = sorted(input_array)
    return input_array.index(s[len(input_array) // 2])
