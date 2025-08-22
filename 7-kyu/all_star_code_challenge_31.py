def help_jesse(arr):
    result = []
    for instr in arr:
        base = f"Pour {instr.amount} mL of {instr.solution} into a {instr.instrument}"
        if hasattr(instr, 'note'):
            result.append(f"{base} ({instr.note})")
        else:
            result.append(base)
    
    return result
