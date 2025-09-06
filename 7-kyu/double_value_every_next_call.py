class Class:
    counter = 0
    
    @staticmethod
    def get_number():
        Class.counter += 1
        return 2 ** (Class.counter - 1)
