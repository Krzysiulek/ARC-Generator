import numpy as np

from combinations.combinationcolor import get_template_color, SOLUTION_COLOR
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import square_generator, create_empty


class CropSmallestModel:
    def __init__(self, position, size):
        self.position = position
        self.size = size


class CropSmallestGenerator(GeneratorInterface):
    def __init__(self,
                 width,
                 height,
                 smallest_position,
                 smallest_size,
                 big_squares):
        self.width = width
        self.height = height

        self.smallest_position = smallest_position
        self.smallest_size = smallest_size
        self.smallest_color = 1
        self.big_squares = big_squares

    def generate_input(self):
        image = create_empty(self.height, self.width)

        for idx, square in enumerate(self.big_squares):
            image = square_generator(image, square.position, square.size, get_template_color(idx))

        image = square_generator(image, self.smallest_position, self.smallest_size, SOLUTION_COLOR)
        return image

    def generate_output(self):
        image = np.full((self.smallest_size, self.smallest_size), SOLUTION_COLOR, dtype=np.chararray)
        return image


class CropSmallestVariationsGenerator:

    def generate_all(self):
        possible_values = []

        heights = [4, 5, 6, 7, 8]
        widths = [4, 5, 6, 7, 8]
        smallest_sizes = [1, 2, 3]
        max_bigger_amount = 3

        for height in heights:
            for width in widths:
                for small_size in smallest_sizes:
                    for small_x_position in range(0, width - small_size):
                        for small_y_position in range(0, height - small_size):
                            for bigger_amount in range(0, max_bigger_amount):
                                for bigger_size in range(small_size + 1, min(height, width)):

                                    bigger = self.generate_bigger(bigger_amount, bigger_size)
                                    csg = CropSmallestGenerator(width=width,
                                                                height=height,
                                                                smallest_position=(small_y_position, small_x_position),
                                                                smallest_size=small_size,
                                                                big_squares=bigger)

                                    possible_values.append(csg)


        return possible_values



    def generate_bigger(self, bigger_max_amount, bigger_size):
        bigger = []

        for _ in range(0, bigger_max_amount):
            csm = CropSmallestModel((0, 0), bigger_size)
            bigger.append(csm)

        return bigger