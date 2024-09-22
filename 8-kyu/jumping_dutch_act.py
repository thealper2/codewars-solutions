def sc(n: int) -> str:
    if n < 2:
        return ""
    elif n <= 6:
        return ''.join(["Aa~ " for _ in range(n-1)]) + "Pa! Aa!"
    elif n > 6:
        return ''.join(["Aa~ " for _ in range(n-1)]) + "Pa!" 