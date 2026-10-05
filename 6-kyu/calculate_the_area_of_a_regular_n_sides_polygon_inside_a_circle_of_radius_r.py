import math

def area_of_inscribed_polygon(circle_radius, number_of_sides):
    return (
        number_of_sides
        / 2
        * circle_radius ** 2
        * math.sin(2 * math.pi / number_of_sides)
    )