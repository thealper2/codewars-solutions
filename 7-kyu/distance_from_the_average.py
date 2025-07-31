def distances_from_average(test_list):
    avg = sum(test_list) / len(test_list)
    return [round(avg - item, 2) for item in test_list]
