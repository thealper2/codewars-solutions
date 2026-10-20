def diag_2_sym(strng):
    lines = strng.split('\n')
    n = len(lines)
    return '\n'.join(
        ''.join(lines[n - 1 - j][n - 1 - i] for j in range(n))
        for i in range(n)
    )

def rot_90_counter(strng):
    lines = strng.split('\n')
    n = len(lines)
    return '\n'.join(
        ''.join(lines[j][n - 1 - i] for j in range(n))
        for i in range(n)
    )

def selfie_diag2_counterclock(strng):
    lines = strng.split('\n')
    d2 = diag_2_sym(strng).split('\n')
    rc = rot_90_counter(strng).split('\n')
    return '\n'.join(f"{lines[i]}|{d2[i]}|{rc[i]}" for i in range(len(lines)))

def oper(fct, s):
    return fct(s)