import numpy as np


def create_empty(height, width):
    size = (height, width)
    image = np.zeros(size, dtype=np.chararray)
    return image


def square_generator(image, square_position, square_size, square_color):
    for x in range(0, square_size):
        for y in range(0, square_size):
            x_pos = square_position[0] + x
            y_pos = square_position[1] + y

            image[x_pos][y_pos] = square_color

    return image


def create_dot(image, width_position, height_position, color):
    image[width_position][height_position] = color
    return image


def create_frame(image, color):
    # poziome kreski
    image[0] = color
    image[len(image) - 1] = color

    # pionowe kreski
    for val in image:
        val[0] = color
        val[-1] = color

    return image
