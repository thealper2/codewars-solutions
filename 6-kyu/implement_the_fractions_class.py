from math import gcd

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    def __str__(self):
        return f'{self.top}/{self.bottom}'
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        g = gcd(new_top, new_bottom)
        return Fraction(new_top // g, new_bottom // g)