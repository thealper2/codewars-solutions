import math


def sensor_analysis(sensor_data):
    n = len(sensor_data)
    mean = 0.0
    std_dev = 0.0
    
    for data in sensor_data:
        distance = data[1]
        mean += distance / n
    
    for data in sensor_data:
        distance = data[1]
        std_dev += math.pow(distance - mean, 2)
    
    std_dev = math.sqrt(std_dev / (n - 1))
    mean = round(mean, 4)
    std_dev = round(std_dev, 4)
    return (mean, std_dev)
