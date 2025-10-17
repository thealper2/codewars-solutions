def sequence_sum(begin, end, step):
    if (begin > end and step > 0) or (begin < end and step < 0):
        return 0
    
    n = (end - begin) // step + 1
    return n * begin + step * n * (n - 1) // 2
