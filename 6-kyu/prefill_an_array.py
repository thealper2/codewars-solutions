def prefill(n=0, v=None) -> list:
    if isinstance(n, (float, bool)):
        raise TypeError(f"{n} is invalid")
    try:
        n = int(n)
    except (ValueError, TypeError):
        raise TypeError(f"{n} is invalid")
    if n < 0:
        raise TypeError(f"{n} is invalid")
    return [v] * n