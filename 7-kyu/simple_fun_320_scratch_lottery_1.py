def scratch(lottery):
    result = 0
    for x in lottery:
        words = x.split()
        reward = int(words[-1])
        temp = words[0]
        found = True
        for word in words[1:-1]:
            if word != temp:
                found = False
                break

        if found:
            result += reward

    return result
