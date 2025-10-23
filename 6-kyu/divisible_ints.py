def get_count(N):
    n_str = str(N)
    count = 0
    for i in range(len(n_str)):
        for j in range(i + 1, len(n_str) + 1):
            substr = n_str[i:j]
            num = int(substr)
            if num == 0:
                continue
            
            if num == N:
                continue
            
            if N % num == 0:
                count += 1
    
    return count
