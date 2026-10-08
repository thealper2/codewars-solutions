class Converter():
    @staticmethod
    def to_ascii(h):
        return bytes.fromhex(h).decode('ascii')

    @staticmethod
    def to_hex(s):
        return s.encode('ascii').hex()