class Harshad:
    @staticmethod
    def is_valid(number):
        if number <= 0:
            return False
        
        return number % sum(int(d) for d in str(number)) == 0
    
    @staticmethod
    def get_next(number):
        number += 1
        while not Harshad.is_valid(number):
            number += 1
            
        return number
    
    @staticmethod
    def get_series(count, start=0):
        result = []
        current = start
        while len(result) < count:
            current = Harshad.get_next(current)
            result.append(current)
            
        return result