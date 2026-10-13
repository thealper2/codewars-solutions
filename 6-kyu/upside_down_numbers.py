def solve(a, b):
    valid = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    def is_upside_down(n):
        s = str(n)
        rotated = []
        for ch in reversed(s):
            if ch not in valid:
                return False
            rotated.append(valid[ch])
        return ''.join(rotated) == s
    
    return sum(1 for n in range(a, b) if is_upside_down(n))