class PrimeFactorizer:
    def __init__(self, n: int):
        self.factor = {}
        d = 2
        while d * d <= n:
            while n % d == 0:
                self.factor[d] = self.factor.get(d, 0) + 1
                n //= d

            d += 1

        if n > 1:
            self.factor[n] = self.factor.get(n, 0) + 1