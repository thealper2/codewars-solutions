def take_while(arr, pred_fun):
    result = []
    for item in arr:
        if pred_fun(item):
            result.append(item)
        else:
            break
            
    return result