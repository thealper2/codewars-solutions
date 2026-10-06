def find_in_array(seq, predicate): 
    result = [i for i, s in enumerate(seq) if predicate(s, i)]
    return result[0] if result else -1a