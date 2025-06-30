def is_loch_ness_monster(string):
    return (
        "tree fiddy" in string.lower()
        or "3.50" in string.lower()
        or "three fifty" in string.lower()
    )
