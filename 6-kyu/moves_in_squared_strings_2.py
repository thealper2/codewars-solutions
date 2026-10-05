def rot(strng):
    return '\n'.join(word[::-1] for word in strng.split('\n')[::-1])

def selfie_and_rot(strng):
    return '\n'.join(word + '.' * len(word) for word in strng.split('\n')) + '\n' + '\n'.join('.' * len(word) + word for word in rot(strng).split('\n'))

def oper(fct, s):
    return fct(s)