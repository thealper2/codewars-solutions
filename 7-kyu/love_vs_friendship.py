def words_to_marks(s):
    return sum(ord(c) - ord('a') + 1 for c in s)
