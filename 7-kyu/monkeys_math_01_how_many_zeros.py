import re


def countzero(s):
    s = re.sub(r"[abdegopq069DOPQR]", "0", s)
    s = re.sub(r"\(\)", "0", s)
    s = re.sub(r"[%&B8]", "00", s)
    return s.count("0")
