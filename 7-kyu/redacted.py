def redacted(doc1, doc2):
    if len(doc1) != len(doc2):
        return False

    for a, b in zip(doc1, doc2):
        if a != "X" and a != b:
            return False

        if a == "X" and b == "\n":
            return False
    return True
