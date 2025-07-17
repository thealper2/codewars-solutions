def multiply_all(arr):
    def multiplier(n):
        return [x * n for x in arr]
    
    return multiplier
