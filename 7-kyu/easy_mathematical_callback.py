def process_array(arr, callback):
    return [callback(item) for item in arr]
