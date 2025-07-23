def are_similar(A, B):
    if A == B:
        return True
    
    differences = []
    for i in range(len(A)):
        if A[i] != B[i]:
            differences.append(i)
    
    if len(differences) != 2:
        return False
    
    i, j = differences
    return A[i] == B[j] and A[j] == B[i]