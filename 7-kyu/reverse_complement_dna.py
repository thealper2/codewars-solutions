def reverse_complement(dna):
    result = ''
    for c in dna:
        if c == 'T':
            result += 'A'
        elif c == 'A':
            result += 'T'
        elif c == 'G':
            result += 'C'
        elif c == 'C':
            result += 'G'
        else:
            return "Invalid sequence"
        
    return result[::-1]
