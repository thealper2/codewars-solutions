class Cipher:
    def __init__(self, map1, map2):
        self.enc = {m1: m2 for m1, m2 in zip(map1, map2)}
        self.dec = {m2: m1 for m1, m2 in self.enc.items()}

    def encode(self, string):
        return ''.join(self.enc.get(c, c) for c in string)

    def decode(self, string):
        return ''.join(self.dec.get(c, c) for c in string)