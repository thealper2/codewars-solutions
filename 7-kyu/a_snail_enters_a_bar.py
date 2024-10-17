def can_snail_reach_end(length, speed, length_increases):
    snail_distance = speed * 60 * 24 * 365
    rubber_band_final = length + length_increases * 60 * 24 * 365
    return snail_distance >= rubber_band_final