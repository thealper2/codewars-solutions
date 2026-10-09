def rot_90_clock(s):
    return '\n'.join(line[::-1] for line in diag_1_sym(s).split('\n'))

def diag_1_sym(s):
    lines = s.split('\n')
    return '\n'.join(''.join(lines[i][j] for i in range(len(lines))) for j in range(len(lines)))


def selfie_and_diag1(s):
    diag = diag_1_sym(s).split('\n')
    lines = s.split('\n')
    return '\n'.join(f'{lines[i]}|{diag[i]}' for i in range(len(lines)))

def oper(fct, s):
    return fct(s)