def to_query_string(data):
    result = []
    for k, v in data.items():
        if isinstance(v, list):
            for item in v:
                result.append(f'{k}={item}')
        else:
            result.append(f'{k}={v}')
        
    return '&'.join(result)
