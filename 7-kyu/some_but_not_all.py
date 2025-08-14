def some_but_not_all(seq, pred): 
    results = [pred(s) for s in seq]
    return True in results and False in results
