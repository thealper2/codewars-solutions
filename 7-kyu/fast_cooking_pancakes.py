def cook_pancakes(n, m):
    if n <= m:
        return 2
    
    return (2 * n + m - 1) // m