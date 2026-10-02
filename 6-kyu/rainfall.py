def _get_records(town, strng):
    for line in strng.split('\n'):
        if not line:
            continue

        name, _, rest = line.partition(':')
        if name == town:
            values = []
            for item in rest.split(','):
                item = item.strip()
                parts = item.split()
                if len(parts) == 2:
                    values.append(float(parts[1]))

            return values

    return None

def mean(town, s):
    vals = _get_records(town, s)
    if not vals:
        return -1.0

    return sum(vals) / len(vals)

def variance(town, s):
    vals = _get_records(town, s)
    if not vals:
        return -1.0

    m = sum(vals) / len(vals)
    return sum((x - m) ** 2 for x in vals) / len(vals)