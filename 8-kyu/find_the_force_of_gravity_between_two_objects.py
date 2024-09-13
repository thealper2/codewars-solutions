def solution(arr_val, arr_unit):
    mass = {"kg": 1, "g": 0.001, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592}
    distance = {"m": 1, "cm": 0.01, "mm": 0.001, "μm": 1e-6, "ft": 0.3048}

    G = 6.67e-11

    return G * (mass[arr_unit[0]] * arr_val[0]) * (mass[arr_unit[1]] * arr_val[1]) / (distance[arr_unit[2]] * arr_val[2]) ** 2