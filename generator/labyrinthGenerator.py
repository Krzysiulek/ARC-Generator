from combinations.combinationcolor import SOLUTION_COLOR
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty


class LabyrinthGenerator(GeneratorInterface):
    def __init__(self,
                 width,
                 height):
        self.width = width
        self.height = height

    def generate_input(self):
        image = create_empty(self.height, self.width)
        return image

    def generate_output(self):
        it = 0
        it_to_stop = 0
        image = create_empty(self.height, self.width)
        image[image == 0] = 1
        point = (1, 0)

        should_stop = False

        while (not should_stop):
            if it == 0:
                point = go_right(image, point)
            if it == 1:
                point = go_down(image, point)
                image[self.height - 2][self.width - 2] = 0
            if it == 2:
                point = go_left(image, point)
            if it == 3:
                point = go_up(image, point)

            it += 1

            if it == 4:
                it = 0

            it_to_stop += 1
            if it_to_stop == self.width - 2:
                should_stop = True

        image[image == 1] = SOLUTION_COLOR
        return image


class LabyrinthVariationsGenerator:

    def generate_all(self):
        possible_values = []

        for height in range(6, 33):
            for width in range(6, 33):
                if width != height:
                    continue

                generator = LabyrinthGenerator(width=width,
                                               height=height)
                possible_values.append(generator)

        return possible_values


def go_right(image, starting_point):
    end_y = starting_point[0]
    end_x = len(image[0]) - 2

    for x in range(starting_point[1], len(image[end_y]) - 1):
        if x + 2 == len(image[0]):
            continue

        point = image[end_y][x + 2]
        image[end_y][x] = 0

        if point == 0:
            end_x = x
            break

    return (end_y, end_x)


def go_down(image, starting_point):
    end_y = len(image) - 2
    end_x = starting_point[1]

    for y in range(starting_point[0], len(image) - 1):
        if y + 2 == len(image):
            continue

        point = image[y + 2][end_x]
        image[y][end_x] = 0

        if point == 0:
            end_y = y
            break

    return (end_y, end_x)


def go_left(image, starting_point):
    end_y = starting_point[0]
    end_x = 1

    for x in reversed(range(end_x, starting_point[1])):
        point = image[end_y][x - 2]
        image[end_y][x] = 0

        if point == 0:
            end_x = x
            break

    return (end_y, end_x)


def go_up(image, starting_point):
    end_y = 1
    end_x = starting_point[1]

    for y in reversed(range(end_y, starting_point[0])):
        if y - 2 == len(image):
            continue

        point = image[y - 2][end_x]
        image[y][end_x] = 0

        if point == 0:
            end_y = y
            break

    return (end_y, end_x)
