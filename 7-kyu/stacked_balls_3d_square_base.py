import math


def stack_height_3d(layers):
    if layers == 0:
        return 0

    return 1 + (layers - 1) * math.sqrt(2) / 2 if layers > 1 else 1
