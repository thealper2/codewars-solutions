from preloaded import FILTERS


def is_valid(query: str) -> bool:
    words = query.split()
    for word in words:
        if ':' in word:
            q = word.split(':')[0]
            if q not in FILTERS:
                return False
            
    return True
