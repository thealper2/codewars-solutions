def solution(args):
    result = []
    i = 0
    n = len(args)
    while i < n:
        j = i
        while j + 1 < n and args[j + 1] == args[j] + 1:
            j += 1

        length = j - i + 1
        if length >= 3:
            result.append(f"{args[i]}-{args[j]}")
        else:
            for k in range(i, j + 1):
                result.append(str(args[k]))
        i = j + 1

    return ','.join(result)