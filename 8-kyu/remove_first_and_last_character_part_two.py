def array(string):
    arr = string.split(",")
    if len(arr) < 3:
        return None
    else:
        return ' '.join(arr[1:len(arr)-1])