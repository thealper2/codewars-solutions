def pass_the_door_man(word):
    n = len(word)
    identical = None
    for i in range(1, n):
        if word[i] == word[i - 1]:
            identical = word[i - 1]
            break

    return (ord(identical) - ord("a") + 1) * 3
