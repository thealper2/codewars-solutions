def cross_product(a, b):
    return Vector(
        x=(a.y * b.z) - (a.z * b.y),
        y=(a.z * b.x) - (a.x * b.z),
        z=(a.x * b.y) - (a.y * b.x),
    )
