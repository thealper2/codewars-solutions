def to_1D(x, y, size):
    width, height = size
    return y * width + x
    
def to_2D(n, size):
    width, height = size
    x = n % width
    y = n // width
    return (x, y)
