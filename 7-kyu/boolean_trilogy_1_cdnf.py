def cdnf(truth_table):
    n = len(truth_table[0]) - 1
    terms = []
    for row in truth_table:
        if row[-1] == 1:
            term_parts = []
            for i in range(n):
                if row[i] == 0:
                    term_parts.append(f"~x{i + 1}")
                else:
                    term_parts.append(f"x{i + 1}")
                    
            terms.append(" * ".join(term_parts))
                
    return " + ".join(f"({term})" for term in terms)
