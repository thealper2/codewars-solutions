import hashlib


def pass_hash(s):
    return hashlib.md5(s.encode()).hexdigest()
