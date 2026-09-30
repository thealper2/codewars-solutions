def _number(n):
    def inner(op=None):
        return n if op is None else op(n)
    return inner


zero = _number(0)
one = _number(1)
two = _number(2)
three = _number(3)
four = _number(4)
five = _number(5)
six = _number(6)
seven = _number(7)
eight = _number(8)
nine = _number(9)


def plus(b):
    return lambda a: a + b


def minus(b):
    return lambda a: a - b


def times(b):
    return lambda a: a * b


def divided_by(b):
    return lambda a: a // b