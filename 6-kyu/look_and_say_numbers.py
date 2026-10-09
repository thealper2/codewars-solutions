def look_and_say(data='1', maxlen=5):
    result = []
    current = data
    for _ in range(maxlen):
        next_val = []
        i = 0
        while i < len(current):
            j = i
            while j < len(current) and current[j] == current[i]:
                j += 1

            next_val.append(str(j - i))
            next_val.append(current[i])
            i = j

        current = ''.join(next_val)
        result.append(current)

    return result