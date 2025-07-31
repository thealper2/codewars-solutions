def solve(a, b):
    asterisk_index = a.find("*")

    if asterisk_index == -1:
        return a == b
    else:
        prefix = a[:asterisk_index]
        suffix = a[asterisk_index + 1 :]

        if len(prefix) + len(suffix) > len(b):
            return False

        if not b.startswith(prefix):
            return False

        if not b.endswith(suffix):
            return False

        return True
