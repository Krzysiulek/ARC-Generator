import itertools

import numpy as np

from combinations.combinationcolor import SOLUTION_COLOR, get_template_color
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty, create_dot


class RepetitionGenerator(GeneratorInterface):
    def __init__(self,
                 width,
                 height,
                 repetition_points,
                 not_repetition_points):
        self.width = width
        self.height = height
        self.repetition_points = repetition_points
        self.not_repetition_points = not_repetition_points

    def generate_input(self):
        image = create_empty(self.height, self.width)
        self.generate_points(image, 0, 0)
        return image

    def generate_output(self):
        image = create_empty(self.height ** 2, self.width ** 2)

        for point in self.repetition_points:
            image = self.generate_points(image, point[0] * self.height, point[1] * self.width)

        return image

    def generate_points(self, image, offset_x, offset_y):
        for point in self.repetition_points:
            create_dot(image, point[0] + offset_x, point[1] + offset_y, SOLUTION_COLOR)

        for point in self.not_repetition_points:
            create_dot(image, point[0] + offset_x, point[1] + offset_y, get_template_color(0))

        return image


class RepetitionVariationsGenerator:

    def generate_all(self):
        possible_values = []

        heights = [3, 4]
        widths = [3, 4]

        for height in heights:
            for width in widths:
                variations = self.create_variation_points(height, width)
                for points in variations:

                    if not points.__contains__(1):
                        continue

                    if not points.__contains__(2):
                        continue

                    # BACKGROUND: 0
                    # SOLUTION_COLOR: 1
                    # TEMPLATE_COLOR: 2
                    reshaped_points = self.reshape(height, width, points)
                    repetition_points = self.create_points(reshaped_points, 1)
                    not_repetition_points = self.create_points(reshaped_points, 2)

                    generator = RepetitionGenerator(width=width,
                                                    height=height,
                                                    repetition_points=repetition_points,
                                                    not_repetition_points=not_repetition_points)
                    possible_values.append(generator)

        return possible_values

    def reshape(self, height, width, list):
        l2 = np.reshape(list, (height, width)).tolist()
        return l2

    def create_variation_points(self, height, width):
        l = list(itertools.combinations_with_replacement([0, 1, 2], r=height * width))
        return l

    def create_points(self, list_to_search, value_to_find):
        points = []

        for x, sublist in enumerate(list_to_search):
            for y, val in enumerate(sublist):
                if val == value_to_find:
                    points.append((x, y))

        return points
