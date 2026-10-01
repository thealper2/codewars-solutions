def sum_strings(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        da = ord(a[i]) - 48 if i >= 0 else 0
        db = ord(b[j]) - 48 if j >= 0 else 0
        total = da + db + carry
        result.append(chr(total % 10 + 48))
        carry = total // 10
        i -= 1
        j -= 1

    while len(result) > 1 and result[-1] == '0':
        result.pop()

    return ''.join(reversed(result)) if result else '0'