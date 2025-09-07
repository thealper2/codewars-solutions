def symmetric_shape(shape, q):
    qx, qy = q
    reflected = [(2 * qx - x, 2 * qy - y) for x, y in shape]
    return shape + reflected
