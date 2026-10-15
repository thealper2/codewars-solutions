def solve(s):
    count = 0
    for i in range(len(s)):
        if int(s[i]) % 2 == 1:
            count += i + 1

    return count