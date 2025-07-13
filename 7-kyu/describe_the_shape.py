def describe_the_shape(angles):
    if angles <= 2:
        return "this will be a line segment or a dot"
    
    sides = angles
    angle = (angles - 2) * 180 // angles
    return f"This shape has {sides} sides and each angle measures {angle}"