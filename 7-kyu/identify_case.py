def case_id(c_str):
    if '-' in c_str and '_' not in c_str:
        parts = c_str.split('-')
        if all(part.isalpha() and part.islower() for part in parts) and len(parts) > 1 and '' not in parts:
            return "kebab"
        
    elif '_' in c_str and '-' not in c_str:
        parts = c_str.split('_')
        if all(part.isalpha() and part.islower() for part in parts) and len(parts) > 1 and '' not in parts:
            return "snake"
    
    elif c_str and c_str[0].islower() and c_str.isalpha():
        if any(c.isupper() for c in c_str):
            return "camel"
    
    return "none"
