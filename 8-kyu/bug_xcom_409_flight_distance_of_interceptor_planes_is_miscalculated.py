def travel_distance(avg_speed, travel_time):
    KNOTS_TO_KMH = 1.852
    travel_hours = travel_time / 60
    travel_miles = avg_speed * travel_hours
    travel_kms = travel_miles * KNOTS_TO_KMH
    return travel_kms