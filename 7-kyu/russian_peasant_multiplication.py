def multiply(a,b):
    total = 0
    counter = 0
    while counter < b:
        total += a
        counter += 1
        
    return total

def russian_peasant_multiplication(x, y):
    product = 0
    while y != 0:
        if y % 2 == 1:
            product = product + x
        
        x = multiply(x, 2)
        y = y // 2
        
    return product
