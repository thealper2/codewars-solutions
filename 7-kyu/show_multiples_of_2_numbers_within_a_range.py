def multiples(s1,s2,s3):
    return [i for i in range(min(s1, s2), s3) if i % s1 == 0 and i % s2 == 0]
