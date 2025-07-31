def vaporcode(s):
    return "  ".join(c.upper() for c in s if c != " ")
