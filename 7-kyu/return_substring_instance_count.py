def solution(full_text: str, search_text: str) -> int:
    count = 0
    i = 0
    n = len(search_text)
    if n == 0:
        return 0
    
    while i <= len(full_text) - n:
        if full_text[i:i+n] == search_text:
            count += 1
            i += n
        else:
            i += 1
    return count
