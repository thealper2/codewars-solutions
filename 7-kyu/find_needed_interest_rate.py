from decimal import Decimal, getcontext


def required_interest_rate(initial, target, years, period):
    if initial == target:
        return Decimal("0")

    getcontext().prec = 28

    P = initial
    A = target
    t = Decimal(years)
    n_compounding = Decimal(period)
    exponent = 1 / (n_compounding * t)
    ratio = A / P
    root = ratio**exponent
    r = n_compounding * (root - 1)
    r_percent = r * Decimal("100")
    return r_percent
