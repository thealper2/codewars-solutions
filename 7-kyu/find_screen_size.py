def find_screen_height(width, ratio): 
    h_ratio, w_ratio = map(int, ratio.split(':'))
    height = int((int(width) / h_ratio) * w_ratio)
    return str(width) + "x" + str(height)