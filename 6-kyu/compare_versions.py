def compare_versions(version1,version2):
    v1 = [int(x) for x in version1.split('.')]
    v2 = [int(x) for x in version2.split('.')]
    n = max(len(v1), len(v2))
    v1 += [0] * (n - len(v1))
    v2 += [0] * (n - len(v2))
    return v1 >= v2