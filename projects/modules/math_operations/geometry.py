"""
    Calculates area of a rectange, triangle, and circle
"""


def traingle_area_calculate(base, height):
    """
    calculates triangle areas

    Args:
        base (float): base of triangle
        height (float): height of triangle

    Returns:
        float: calculated area
    """
    area = 1/2(base * height)
    return area


def square_area_calculate(base, height):
    """
    calculates square areas

    Args:
        base (float): base of square
        height (float): height of square

    Returns:
        float: calculated area
    """
    area = (base * height)
    return area


def circle_area_calculate(radius):
    """
    calculates area of a circle

    Args:
        radius (float): radius of the circle

    Returns:
        float: area of circle
    """
    area = 3.14 * (radius ** 2)
    return area
