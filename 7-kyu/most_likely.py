def most_likely(prob1: str, prob2: str) -> bool:
    a, b = map(int, prob1.split(':'))
    c, d = map(int, prob2.split(':'))
    return a * d > c * b