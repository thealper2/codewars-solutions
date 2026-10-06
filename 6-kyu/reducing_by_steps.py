import math

def gcdi(x,y):
    return math.gcd(abs(x), abs(y))
    
def lcmu(a, b):
    return math.lcm(abs(a), abs(b))

def som(a, b):
    return a + b

def maxi(a, b):
    return max(a, b)

def mini(a, b):
    return min(a, b)

def oper_array(fct, arr, init): 
    result = [init]
    for item in arr:
        val = fct(item, result[-1])
        result.append(val)
        
    return result[1:]