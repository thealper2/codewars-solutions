def agents(list_found, list_records):
    if not list_found:
        return None
    
    l = len(list_found)
    for record in list_records:
        n = len(record)
        if n == l:
            is_found = True
            for a, b in zip(list_found, record):
                if a != b:
                    is_found = False
                    
            if is_found:
                return "Match found"
            
    return "No matches"
