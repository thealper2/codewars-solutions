class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other_name):
        return f"Hello {other_name}, my name is {self.name}"
