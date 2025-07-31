def archers_ready(archers):
    if not archers:
        return False

    return all(archer >= 5 for archer in archers)
