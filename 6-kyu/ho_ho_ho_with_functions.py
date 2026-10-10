class Ho:
    def __init__(self, count=1):
        self.count = count

    def __str__(self):
        return ' '.join(['Ho'] * self.count) + '!'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


def ho(arg=None):
    if arg is None:
        return Ho(1)
    return Ho(arg.count + 1)