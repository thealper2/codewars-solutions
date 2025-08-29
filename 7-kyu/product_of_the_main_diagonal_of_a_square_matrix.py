def main_diagonal_product(mat):
    prod = 1
    n = len(mat)
    for i in range(n):
        prod *= mat[i][i]
        
    return prod
