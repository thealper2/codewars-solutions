def center(mat):
    if not mat:
        return None

    rows = len(mat)
    cols = len(mat[0])
    if rows % 2 == 0 or cols % 2 == 0:
        return None
    return mat[rows // 2][cols // 2]