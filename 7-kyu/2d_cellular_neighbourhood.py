def get_neighbourhood(neighborhood_type, matrix, coordinates):
    m, n = coordinates
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])
    
    if m < 0 or m >= rows or n < 0 or n >= cols:
        return []
    
    neighbors = []
    if neighborhood_type == "moore":
        for i in range(m-1, m+2):
            for j in range(n-1, n+2):
                if (i != m or j != n) and 0 <= i < rows and 0 <= j < cols:
                    neighbors.append(matrix[i][j])
    elif neighborhood_type == "von_neumann":
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for di, dj in directions:
            ni, nj = m + di, n + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                neighbors.append(matrix[ni][nj])
    
    return neighbors
