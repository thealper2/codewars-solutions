class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def greet(self):
        return f"Hello, {self.first} {self.last}!"
