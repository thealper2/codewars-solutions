def make_model_year(lst):
    result = {}
    for item in lst:
        if item == True or item == False:
            result['new'] = item  
        elif isinstance(item, str):
            result['make'] = item
        elif isinstance(item, tuple):
            result['model'] = ' '.join(item)
        elif isinstance(item, int):
            result['year'] = item
    result = {
        'make': result['make'],
        'model': result['model'],
        'year': result['year'],
        'new': result['new']
    }
    return result
            
