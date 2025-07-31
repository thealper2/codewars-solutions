from typing import Callable


def add(n: int) -> Callable:
    return lambda x: x + n
