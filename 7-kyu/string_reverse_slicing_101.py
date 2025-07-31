def reverse_slice(s):
    return [s[:i][::-1] for i in range(len(s), 0, -1)]
