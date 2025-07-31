def reach_destination(distance, speed):
    time = round(2 * distance / speed) / 2
    return "The train will be there in %g hour%s." % (time, "s" * (time != 1))
