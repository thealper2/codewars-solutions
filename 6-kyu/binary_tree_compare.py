def compare(a, b):
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    return (a.val == b.val
            and compare(a.left, b.left)
            and compare(a.right, b.right))