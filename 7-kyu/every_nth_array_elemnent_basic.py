def every(array, interval=1, start_index=0):
    return [array[i] for i in range(start_index, len(array), interval)]