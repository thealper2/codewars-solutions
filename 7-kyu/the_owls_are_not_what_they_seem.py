def owl_pic(text):
    allowed = "8WTYUIOAHXVM"
    plumage = ''.join(c for c in text.upper() if c in allowed)
    return plumage + "''0v0''" + plumage[::-1]
