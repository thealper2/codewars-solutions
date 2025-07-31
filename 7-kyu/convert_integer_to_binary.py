def to_binary(n):
    if n == 0:
        return "0"

    bits = []
    if n > 0:
        while n > 0:
            bits.append(str(n % 2))
            n = n // 2
        binary = "".join(reversed(bits))
    else:
        positive = -n
        binary = ""
        for _ in range(32):
            binary = str(positive % 2) + binary
            positive = positive // 2

        inverted = "".join(["1" if bit == "0" else "0" for bit in binary])
        carry = 1
        twos_complement = []
        for bit in reversed(inverted):
            if bit == "0" and carry == 1:
                twos_complement.append("1")
                carry = 0
            elif bit == "1" and carry == 1:
                twos_complement.append("0")
            else:
                twos_complement.append(bit)

        twos_complement = "".join(reversed(twos_complement))
        binary = twos_complement.lstrip("0")

    return binary
