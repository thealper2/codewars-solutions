from fractions import Fraction

def sum_fracts(lst):
    if not lst:
        return None
    
    total = sum(Fraction(n, d) for n, d in lst)
    if total.denominator == 1:
        return total.numerator
    
    return [total.numerator, total.denominator]