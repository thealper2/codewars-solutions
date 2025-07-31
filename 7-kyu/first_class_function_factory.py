def factory(x):
    def multiplier(arr):
        return [x * item for item in arr]

    return multiplier
