def largest(n, xs):
    result = []
    while n:
        max_ = max(xs)
        result.append(max_)
        xs.remove(max_)
        n -= 1
    
    return result[::-1]
