def convert_lojban(lojban):
    n = len(lojban)
    lojban_dict = {
        "pa": 1,
        "re": 2,
        "ci": 3,
        "vo": 4,
        "mu": 5,
        "xa": 6,
        "ze": 7,
        "bi": 8,
        "so": 9,
        "no": 0
    }
    result = ""
    
    for i in range(0, n, 2):
        result += str(lojban_dict[lojban[i:i+2]])
        
    return int(result)
