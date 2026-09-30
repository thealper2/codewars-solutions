def format_duration(seconds):
    if seconds == 0:
        return "now"

    units = [
        ("year", 365 * 24 * 3600),
        ("day", 24 * 3600),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1),
    ]

    parts = []
    for name, secs in units:
        value, seconds = divmod(seconds, secs)
        if value:
            parts.append(f"{value} {name}" + ("s" if value != 1 else ""))

    if len(parts) == 1:
        return parts[0]
    
    return ", ".join(parts[:-1]) + " and " + parts[-1]