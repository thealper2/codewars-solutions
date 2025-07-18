import re


def solve(s:str) -> int:
    numbers = re.findall(r'\d+', s)
    if not numbers:
        return 0
    
    return max(map(int, numbers))
