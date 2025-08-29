def categorize_study(p_value, requirements):
    bs_factor = 2 ** (6 - requirements)
    product = p_value * bs_factor
    if product < 0.05:
        if requirements == 0:
            return "Needs review"
        else:
            return "Fine"
        
    elif product < 0.15:
        return "Needs review"
    
    else:
        return "Pants on fire"
