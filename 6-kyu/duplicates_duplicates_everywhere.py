def remove_duplicate_ids(obj):
    keys = sorted(obj.keys(), key=lambda k: int(k), reverse=True)
    seen = set()
    result = {}
    for k in keys:
        kept = []
        for ch in obj[k]:
            if ch not in seen:
                kept.append(ch)
                seen.add(ch)
        
        result[k] = kept
        
    return result