def solution(s):
    return ''.join(c if c.islower() else ' ' + c for c in s)