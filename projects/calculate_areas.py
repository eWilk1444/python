"""
    This will calculate the area of a square and of a circle
"""


def square(side):
    """ This function finds the area of a square

    Args:
        side (float): one side of the square
    """
    area_square = float(side) * float(side)
    # prints to terminal and terminates function
    print(f"The area of the square is {area_square} square units.")


# invoking square function with float
square(10)


def circle(radius):
    """ Finds the area of a circle using 3.14 as a pi approximation 

    Args:
        radius (float): the radius of the circle
    """
    area_circle = float(radius) ** 2 * 3.14
    # prints to terminal and terminates function
    print(f"The area of the circle is {area_circle:.2f} square units.")


# invoking circle function with float
circle(9)
