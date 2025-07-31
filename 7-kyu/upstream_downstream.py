def time(distance, boat_speed, stream):
    direction, stream_speed = stream.split()
    stream_speed = int(stream_speed)

    if direction == "Downstream":
        effective_speed = boat_speed + stream_speed
    elif direction == "Upstream":
        effective_speed = boat_speed - stream_speed
    else:
        return 0.0

    time = distance / effective_speed
    return round(time, 2)
