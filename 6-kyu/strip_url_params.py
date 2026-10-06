def strip_url_params(url, params_to_strip=None):
    if params_to_strip is None:
        params_to_strip = []
        
    strip_set = set(params_to_strip)
    
    if '?' not in url:
        return url
    
    base, _, query = url.partition('?')
    if not query:
        return url
    
    seen = set()
    kept = []
    for pair in query.split('&'):
        if not pair:
            continue
            
        key = pair.split('=', 1)[0]
        if key in seen:
            continue
            
        seen.add(key)
        if key in strip_set:
            continue
            
        kept.append(pair)
        
    if not kept:
        return base
    
    return base + '?' + '&'.join(kept)