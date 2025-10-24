def convert_temp(temp, from_scale, to_scale):
    TO_CELSIUS = {
        'C': (1, 0),
        'F': (5.0 / 9, -32 * 5.0 / 9),
        'K': (1, -273.15),
        'R': (5.0 / 9, -491.67 * 5.0 / 9),
        'De': (-2.0 / 3, 100),
        'N': (100.0 / 33, 0),
        'Re': (5.0 / 4, 0),
        'Ro': (40.0 / 21, -7.5 * 40.0 / 21),
    }
    
    if from_scale == to_scale:
        return round(temp)
    
    if from_scale != 'C':
        a, b = TO_CELSIUS[from_scale]
        temp_celsius = a * temp + b
    else:
        temp_celsius = temp
    
    if to_scale == 'C':
        return round(temp_celsius)
    
    a, b = TO_CELSIUS[to_scale]
    result = (temp_celsius - b) / a
    return round(result)
