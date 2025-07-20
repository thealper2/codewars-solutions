def haiku_wizard(arr):
    haiku_lines = []
    for line in arr:
        line_words = []
        for num in line:
            syllable = (num // 10) - 1
            index = num % 10
            word = words[syllable][index]
            line_words.append(word)
            
        haiku_lines.append(' '.join(line_words))
        
    return '\n'.join(haiku_lines)