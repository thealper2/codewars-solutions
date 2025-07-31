import math
from typing import Tuple


def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    return tuple([math.ceil(16 * y / 9), y])
