def lineup_students(s):
    if not s.strip():
        return []
    
    names = s.split()
    return sorted(sorted(names, reverse=True), reverse=True, key=len)