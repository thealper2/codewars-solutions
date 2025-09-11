def find_e(s):
    if s == None:
        return None
    
    if not s:
        return ''
    
    e_count = s.count('e')
    e_count += s.count('E')
    if e_count == 0:
        return "There is no \"e\"."
    
    return str(e_count)
