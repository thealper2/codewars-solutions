def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled) / (
        blue_start + red_start - red_pulled - blue_pulled
    )
