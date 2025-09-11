def score_matrix(matrix):
    return sum(((-1) ** (i + j)) * val 
               for i, row in enumerate(matrix) 
               for j, val in enumerate(row))
