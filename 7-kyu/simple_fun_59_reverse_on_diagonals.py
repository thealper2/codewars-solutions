def reverse_on_diagonals(matrix):
    n = len(matrix)
    main_diagonal = [matrix[i][i] for i in range(n)][::-1]
    anti_diagonal = [matrix[i][n - 1 - i] for i in range(n)][::-1]
    
    for i in range(n):
        matrix[i][i] = main_diagonal[i]
        matrix[i][n - 1 - i] = anti_diagonal[i]
        
    return matrix
