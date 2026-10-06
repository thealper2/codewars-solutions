def name_in_str(strng : str, name : str) -> bool:
    it = iter(strng.lower())
    return all(c in it for c in name.lower())