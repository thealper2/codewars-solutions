def decrypt(test_key):
    counts = [0] * 26
    for ch in test_key:
        if 'a' <= ch <= 'z':
            counts[ord(ch) - ord('a')] += 1
            
    return ''.join(str(c) for c in counts)