def solve(s):
    new_s = s.translate(str.maketrans({'a': ' ', 'e': ' ', 'i': ' ', 'o': ' ', 'u': ' '}))
    words = [word.strip() for word in new_s.split() if word]
    max_cons = max([sum(ord(c) - ord('a') + 1 for c in word) for word in words])
    return max_cons
    