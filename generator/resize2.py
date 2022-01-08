import itertools

import numpy as np

from combinations.combinationcolor import SOLUTION_COLOR, get_template_color
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty, create_dot


class ResizeGenerator(GeneratorInterface):
    def __init__(self,
                 width,
                 height,
                 starting_input):
        self.width = width
        self.height = height
        self.starting_input = starting_input

    def generate_input(self):
        image = create_empty(self.height, self.width)

        # pozamieniaj na template_color
        for x, var in enumerate(self.starting_input):
            for y, point in enumerate(var):
                if point == 0:
                    image[x][y] = 0
                else:
                    image[x][y] = get_template_color(point)

        return image

    def generate_output(self):
        image = create_empty(self.height * 2, self.width * 2)

        for x, var in enumerate(self.starting_input):
            for y, point in enumerate(var):
                value_to_put = get_template_color(point)
                new_x = x * 2
                new_y = y * 2

                if point == 0:
                    value_to_put = "0"

                image[new_x][new_y] = value_to_put
                image[new_x + 1][new_y] = value_to_put
                image[new_x][new_y + 1] = value_to_put
                image[new_x + 1][new_y + 1] = value_to_put

        return image


class ResizeVariationsGenerator:

    def generate_all(self):
        possible_values = []

        heights = [3]
        widths = [3]

        for height in heights:
            for width in widths:
                variations = self.create_variation_points(height, width)
                for points in variations:
                    if set(points) == set([0]):
                        continue


                    generator = ResizeGenerator(width=width,
                                                    height=height,
                                                    starting_input=self.reshape(height, width, points))
                    possible_values.append(generator)

        return possible_values

    def reshape(self, height, width, list):
        l2 = np.reshape(list, (height, width)).tolist()
        return l2

    def create_variation_points(self, height, width):
        l = list(itertools.combinations_with_replacement([0, 1, 2, 4, 5], r=height * width))
        return l

    def create_points(self, list_to_search, value_to_find):
        points = []

        for x, sublist in enumerate(list_to_search):
            for y, val in enumerate(sublist):
                if val == value_to_find:
                    points.append((x, y))

        return points
