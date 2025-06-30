def God():
    return [Man(), Woman()]


class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name="Adam"):
        self.name = name


class Woman(Human):
    def __init__(self, name="Eve"):
        self.name = name
