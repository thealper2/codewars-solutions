def bears(x,s):
    pairs = []
    i = 0
    n = len(s)
    while i < n - 1 :
        if (s[i] == 'B' and s[i + 1] == '8') or (s[i] == '8' and s[i + 1] == 'B'):
            pairs.append(s[i] + s[i + 1])
            i += 2
        else:
            i += 1

    result_str = ''.join(pairs)
    num_bears = 2 * len(pairs)
    return [result_str, num_bears >= x]