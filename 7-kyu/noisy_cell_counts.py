def cleaned_counts(data):
    result = [data[0]]
    for i in range(1, len(data)):
        if data[i] < result[-1]:
            result.append(result[-1])
        else:
            result.append(data[i])
            
    return result
