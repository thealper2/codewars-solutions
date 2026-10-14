def inside_out(strng: str) -> str:
    result = []
    for word in strng.split():
        n = len(word)
        mid = n // 2
        if n % 2 == 1:
            a = word[:mid][::-1]
            b = word[mid + 1:][::-1]
            result.append(f'{a}{word[mid]}{b}')
        else:
            a = word[:mid][::-1]
            b = word[mid:][::-1]
            result.append(f'{a}{b}')
            
    return ' '.join(result)