import random

from combinations.combinationcolor import SOLUTION_COLOR, get_template_color
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty, create_dot


class FramedDotsGenerator(GeneratorInterface):
    def __init__(self,
                 width,
                 height,
                 dots_positions):
        self.width = width
        self.height = height
        self.dots_positions = dots_positions

    def generate_input(self):
        image = self.create_base_img()
        return image

    def generate_output(self):
        image = self.create_base_img()

        for dot in self.dots_positions:
            if self.is_point_not_over_image((dot[0] - 1, dot[1])):
                image = create_dot(image, dot[0] - 1, dot[1], get_template_color(1))

            if self.is_point_not_over_image((dot[0] + 1, dot[1])):
                image = create_dot(image, dot[0] + 1, dot[1], get_template_color(1))

            if self.is_point_not_over_image((dot[0] + 1, dot[1] + 1)):
                image = create_dot(image, dot[0] + 1, dot[1] + 1, get_template_color(1))

            if self.is_point_not_over_image((dot[0] - 1, dot[1] + 1)):
                image = create_dot(image, dot[0] - 1, dot[1] + 1, get_template_color(1))

            if self.is_point_not_over_image((dot[0], dot[1] + 1)):
                image = create_dot(image, dot[0], dot[1] + 1, get_template_color(1))

            if self.is_point_not_over_image((dot[0], dot[1] - 1)):
                image = create_dot(image, dot[0], dot[1] - 1, get_template_color(1))

            if self.is_point_not_over_image((dot[0] + 1, dot[1] - 1)):
                image = create_dot(image, dot[0] + 1, dot[1] - 1, get_template_color(1))

            if self.is_point_not_over_image((dot[0] - 1, dot[1] - 1)):
                image = create_dot(image, dot[0] - 1, dot[1] - 1, get_template_color(1))

        return image

    def is_point_not_over_image(self, dot):
        if dot[0] >= 0 and dot[0] < self.height and dot[1] >= 0 and dot[1] < self.width:
            return True
        return False


    def create_base_img(self):
        image = create_empty(self.height, self.width)

        # print(self.dots_positions)
        for point in self.dots_positions:
            image = create_dot(image, point[0], point[1], SOLUTION_COLOR)

        return image


class FramedDotsVariationsGenerator:

    def generate_all(self):
        possible_values = []

        for height in range(6, 12):
            for width in range(6, 12):
                for dot_amount in range(1, 5):
                    for _ in range(10):
                        dots = self.get_dots_positions_combinations(height, width, dot_amount)
                        generator = FramedDotsGenerator(width=width,
                                                        height=height,
                                                        dots_positions=dots)
                        possible_values.append(generator)

        return possible_values

    def get_dots_positions_combinations(self, height, width, dots_number):
        dots_to_return = []

        while (len(dots_to_return) < dots_number):
            dot = (random.randrange(0, height), random.randrange(0, width))

            if self.is_such_dot_possible(dot[0], dot[1], dots_to_return, height, width):
                dots_to_return.append(dot)

        return dots_to_return

    def is_such_dot_possible(self, height_point, width_point, tmp_dots, image_height, image_width):

        for dot in tmp_dots:

            if dot[0] >= image_height:
                return False

            if dot[1] >= image_width:
                return False

            space_between = 2

            if dot[0] - space_between <= height_point <= dot[0] + space_between and dot[
                1] - space_between <= width_point <= dot[1] + space_between:
                return False

            # if dot[1] - space_between <= width_point <= dot[1] + space_between:
            #     return False

        return True
