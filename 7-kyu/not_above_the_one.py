def binary_cleaner(seq): 
    ones = []
    indexes = []
    for i, num in enumerate(seq):
        if num < 2:
            ones.append(num)
        else:
            indexes.append(i)
            
    return (ones, indexes)
