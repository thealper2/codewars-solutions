def arrange(arr):
    def convert_to_grams(weight):
        if weight.endswith('KG'):
            return int(weight[:-2]) * 1000
        elif weight.endswith('G'):
            return int(weight[:-1])
        elif weight.endswith('T'):
            return int(weight[:-1]) * 1000000
        
    return sorted(arr, key=convert_to_grams)
        
