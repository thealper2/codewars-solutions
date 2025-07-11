def same_encryption(s1, s2):
    def encrypt_string(s):
        if len(s) <= 2:
            return s[0] + s[-1] if len(s) == 2 else s
        first = s[0]
        last = s[-1]
        middle_length = len(s) - 2
        num = middle_length
        while num >= 10:
            num = sum(int(d) for d in str(num))
        encrypted = first + (str(num) if middle_length != 0 else '') + last
        return encrypted
    
    return encrypt_string(s1) == encrypt_string(s2)
