def convert_temp(temp, from_scale, to_scale):
    if from_scale == to_scale:
        return temp
    
    if from_scale == 'C':
        celsius = temp
    elif from_scale == 'F':
        celsius = (temp - 32) * 5/9
    elif from_scale == 'K':
        celsius = temp - 273.15
    elif from_scale == 'R':
        celsius = (temp - 491.67) * 5/9
    elif from_scale == 'De':
        celsius = 100 - temp * 2/3
    elif from_scale == 'N':
        celsius = temp * 100/33
    elif from_scale == 'Re':
        celsius = temp * 5/4
    elif from_scale == 'Ro':
        celsius = (temp - 7.5) * 40/21
    
    if to_scale == 'C':
        return int(celsius)
    elif to_scale == 'F':
        return int(celsius * 9/5 + 32)
    elif to_scale == 'K':
        return int(celsius + 273.15)
    elif to_scale == 'R':
        return int((celsius + 273.15) * 9/5)
    elif to_scale == 'De':
        return int((100 - celsius) * 3/2)
    elif to_scale == 'N':
        return int(celsius * 33/100)
    elif to_scale == 'Re':
        return int(celsius * 4/5)
    elif to_scale == 'Ro':
        return int(celsius * 21/40 + 7.5)
