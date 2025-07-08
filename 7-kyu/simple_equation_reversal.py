import re


def solve(eq):
    tokens = re.findall(r'(\d+|[a-zA-Z]+|[\+\-\*/])', eq)
    reversed_tokens = tokens[::-1]
    reversed_eq = ''.join(reversed_tokens)
    return reversed_eq