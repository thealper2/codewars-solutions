from contextlib import suppress


def matching(data):
    with suppress(ZeroDivisionError):
        match data:
            case []: return 0
            case [x]: return int(x)
            case [head, *tail]: return int(head) / int(tail[-1])
