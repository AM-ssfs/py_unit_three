def instructions():
    """
    tells user what this does and how to use
    :return:
    """
    print("This program tells you the surface area of a rectangular prism")
    print("please enter the height, length and width of the prisim")


def get_height():
    """
    gets height and returns it
    :return:
    height
    """
    height = float(input("what is the height? "))
    return height


def get_length():
    """
    gets length and returns it
    :return:
    length
    """
    length = float(input("what is the height? "))
    return length


def get_width():
    """
    gets width and returns it
    :return:
    width
    """
    width = float(input("what is the height? "))
    return width


def rectangle_area(length, width):
    """
    retuns area of rectangle from length and width
    :param length:
    :param width:
    :return:
    """
    return length * width


def total_surface_area(height, length, width):
    """
    gets height, length, width and finds total surface area
    :param height:
    :param length:
    :param width:
    :return:
    total surface area
    """
    side1 = rectangle_area(height, length)
    side2 = rectangle_area(height, width)
    side3 = rectangle_area(width, length)
    total = str((side1 + side2 + side3) * 2)
    return total


def individual_surface_area(height, length, width):
    """
    gets height, length, width and finds each side's area
    :param height:
    :param length:
    :param width:
    :return:
    total surface area
    """
    side1 = str(height * length)
    side2 = str(length * width)
    side3 = str(width * height)
    individual = str("side 1: " + side1 + "    side 2: " + side2 + "    side 3: " + side3 + "     side 5: " + side1 + "    side 5: " + side2 + "    side 2: " + side3 )
    return individual


if __name__ == '__main__':
    instructions()
    length = get_length()
    height = get_height()
    width = get_width()
    print(total_surface_area(height, length, width))
    print(individual_surface_area(height, length, width))

