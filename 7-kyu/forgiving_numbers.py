def find_f1_eq_f2(n,k):
    while True:
        n += 1
        result = n
        while True:
            digits = set(str(result))
            digits = [int(d) for d in digits]
            if max(digits) < k:
                if len(digits) != k:
                    break
                else:
                    return n
            
            result += n
