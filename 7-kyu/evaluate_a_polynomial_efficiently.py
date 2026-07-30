def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    result = 0
    for coeff in coefficients:
        result = result * x + coeff
        
    return result
