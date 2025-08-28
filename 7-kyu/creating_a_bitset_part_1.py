def byte_to_set(byte):
    return {i for i in range(8) if byte & (1 << (7 - i))}
