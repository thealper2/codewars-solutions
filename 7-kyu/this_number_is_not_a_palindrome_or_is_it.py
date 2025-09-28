def is_palindrome(n: int) -> bool:
    b = bin(n)[2:]
    return b == b[::-1]
