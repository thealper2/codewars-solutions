def find_glasses(lst):
    for i in range(len(lst)):
        word = lst[i]
        prev = None
        c = 0
        for j in range(len(word)):
            if word[j] == 'O':
                if prev is None:
                    prev = j
                else:
                    if c > 0:
                        return i
                    else:
                        prev = j
                        c = 0
            elif word[j] == '-' and prev is not None:
                c += 1
            else:
                prev = None
                c = 0
    return -1
