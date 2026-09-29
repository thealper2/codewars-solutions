def data_reverse(data):
    return [bit for i in range(len(data) - 8, -1, -8) for bit in data[i:i+8]]