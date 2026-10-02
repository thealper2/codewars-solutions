def longest_palindrome(s):
    if not s:
        return 0

    max_str = s[0]
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if len(sub) > len(max_str) and sub == sub[::-1]:
                max_str = sub

    return len(max_str)