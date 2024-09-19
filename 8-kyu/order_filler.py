def fillable(stock, merch, n):
    if merch in stock.keys():
        return stock[merch] >= n
    else:
        return False
