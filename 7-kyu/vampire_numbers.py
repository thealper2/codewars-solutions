def vampire_test(x, y):
    if x < 0 and y < 0:
        return False
    
    product = x * y
    abs_x = abs(x)
    abs_y = abs(y)
    abs_product = abs(product)
    fang_digits = sorted(str(abs_x) + str(abs_y))
    product_digits = sorted(str(abs_product))
    return fang_digits == product_digits
