import re


def pseudo_sort(sentence):
    words = re.findall(r"[A-Za-z]+", sentence)
    lower = sorted(w for w in words if w[0].islower())
    upper = sorted((w for w in words if w[0].isupper()), reverse=True)
    return ' '.join(lower + upper)