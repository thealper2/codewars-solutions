def head_smash(arr):
    if arr == '':
        return "Gym is empty"
    
    if isinstance(arr, list):
        if not arr:
            return "Gym is empty"
        
        result = []
        for s in arr:
            if isinstance(s, str):
                result.append(s.replace('O', ' '))
            else:
                return "This isn't the gym!!"
            
        return result
    else:
        return "This isn't the gym!!"
