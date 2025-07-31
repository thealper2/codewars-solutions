def one(xs, f):
    count = 0
    for item in xs:
        if f(item):
            count += 1
            if count > 1:
                return False

    return count == 1
