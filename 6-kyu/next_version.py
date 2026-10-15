def next_version(version):
    parts = [int(p) for p in version.split('.')]
    i = len(parts) - 1
    parts[i] += 1
    while i > 0 and parts[i] >= 10:
        parts[i] = 0
        i -= 1
        parts[i] += 1

    return '.'.join(str(p) for p in parts)