def change_count(change):
    total = sum(CHANGE[c] for c in change.split())
    return f"${total:.2f}"
