from typing import Tuple
import math

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    return tuple([math.ceil(16 * y / 9), y])