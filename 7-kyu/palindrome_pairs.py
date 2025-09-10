def palindrome_pairs(words):
    n = len(words)
    words = [str(word) for word in words]
    result = []
    for i in range(n):
        for j in range(n):
            if i != j and words[i] + words[j] == (words[i] + words[j])[::-1]:
                result.append([i, j])
                
    return result
