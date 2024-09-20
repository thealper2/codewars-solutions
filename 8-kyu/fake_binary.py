def fake_bin(x):
    return ''.join(["0" if int(letter) < 5  else "1" for letter in x])