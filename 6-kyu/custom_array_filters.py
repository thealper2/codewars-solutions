class list(list):
    def even(self):
        return list(x for x in self if isinstance(x, int) and not isinstance(x, bool) and x % 2 == 0)

    def odd(self):
        return list(x for x in self if isinstance(x, int) and not isinstance(x, bool) and x % 2 != 0)

    def under(self, n):
        return list(x for x in self if isinstance(x, int) and not isinstance(x, bool) and x < n)

    def over(self, n):
        return list(x for x in self if isinstance(x, int) and not isinstance(x, bool) and x > n)

    def in_range(self, a, b):
        return list(x for x in self if isinstance(x, int) and not isinstance(x, bool) and a <= x <= b)