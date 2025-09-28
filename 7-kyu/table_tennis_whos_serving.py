def who_is_serving(current_round: int) -> int:
    if ((current_round + 1) // 2) % 2 == 1:
        return 1
    else:
        return 2
