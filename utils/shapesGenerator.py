
# todo
def create_empty():
    pass

def square_generator(image, square_position, square_size, square_color):
    for x in range(0, square_size):
        for y in range(0, square_size):
            x_pos = square_position[0] + x
            y_pos = square_position[1] + y

            image[x_pos][y_pos] = square_color

    return image


