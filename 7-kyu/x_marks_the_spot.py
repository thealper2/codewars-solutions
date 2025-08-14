def x_marks_the_spot(mat):
    result = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 'x':
                if not result:
                    result = [i, j]
                else:
                    return []
                
    return result
