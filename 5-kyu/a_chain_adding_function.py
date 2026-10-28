class CustomInt(int):
    def __call__(self, next_value):
        return CustomInt(self + next_value)

def add(initial_value):
    return CustomInt(initial_value)