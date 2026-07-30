def complete(s):
    for i in range(1, len(s) + 1):
        result = s + s[:i][::-1]

        if result == result[::-1]:
            return result
