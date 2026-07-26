def split_coins(coins, k):
    g1 = coins[:k]
    g2 = coins[k:]
    
    for coin in g1:
        coin.flip()
        
    return g1, g2
