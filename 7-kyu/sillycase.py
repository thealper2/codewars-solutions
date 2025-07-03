def sillycase(silly):
    n = len(silly) - len(silly) // 2
    return silly[:n].lower() + silly[n:].upper()