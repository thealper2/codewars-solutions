def empty_values(lst):
    result = []
    for item in lst:
        if type(item) == int:
            result.append(0)
        elif type(item) == float:
            result.append(0.0)
        elif type(item) == str:
            result.append("")
        elif type(item) == bool:
            result.append(False)
        elif type(item) == list:
            result.append([])
        elif type(item) == tuple:
            result.append(())
        elif type(item) == dict:
            result.append({})
        elif type(item) == set:
            result.append(set())
        else:
            result.append(item)
            
    return result
