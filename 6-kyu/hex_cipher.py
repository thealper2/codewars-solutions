from preloaded import TEXT2HEX

class HexCipher:
    @classmethod
    def encode(cls, s, n):
        for _ in range(n):
            s = ''.join(format(ord(c), '02x') for c in s)

        return s

    @classmethod
    def decode(cls, s, n):
        for _ in range(n):
            s = ''.join(chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2))

        return s