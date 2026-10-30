_cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in _cache:
        return _cache[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    _cache[n] = result
    return result