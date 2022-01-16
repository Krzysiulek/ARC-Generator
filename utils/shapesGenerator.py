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

def create_rectangle(image, start_position, end_position, color):
    for x in range(start_position[1], end_position[1] + 1):
        for y in range(start_position[0], end_position[0] + 1):
            image[y][x] = color

    return image


def create_frame_rectangle(image, starting_point, ending_point, color):
    image = create_rectangle(image, starting_point, ending_point, color)
    image = create_rectangle(image,
                             (starting_point[0] + 1, starting_point[1] + 1),
                             (ending_point[0] - 1, ending_point[1] - 1),
                             0)
    return image


def create_line(image, start_position, end_position, color):
    tmp_start_x = min(start_position[0], end_position[0])
    tmp_end_x = max(start_position[0], end_position[0])
    for x in range(tmp_start_x, tmp_end_x):

        tmp_start_y = min(start_position[1], end_position[1])
        tmp_end_y = max(start_position[1], end_position[1])
        for y in range(tmp_start_y, tmp_end_y):
            image[x][y] = color

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
