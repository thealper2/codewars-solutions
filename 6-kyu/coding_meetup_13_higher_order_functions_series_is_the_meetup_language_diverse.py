def is_language_diverse(lst):
    langs = ['Python', 'Ruby', 'JavaScript']
    counts = {lang: 0 for lang in langs}
    for dev in lst:
        counts[dev['language']] += 1

    values = list(counts.values())
    return max(values) <= 2 * min(values)