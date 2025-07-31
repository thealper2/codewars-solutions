def decode_pass(pass_list, bits):
    password = ""
    for bit in bits.split():
        password += chr(int(bit, 2))

    if password in pass_list:
        return password

    return False
