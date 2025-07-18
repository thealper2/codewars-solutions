class Calculator:
    @staticmethod
    def average(*args):
        args = list(args)
        if not args:
            return 0
        
        return sum(args) / len(args)
