from combinations.combinationcolor import SOLUTION_COLOR, get_template_color
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty, create_dot, create_frame_rectangle


class InsideOutsideSquareDotsGenerator(GeneratorInterface):
    def __init__(self,
                 width,
                 height,
                 starting_point,
                 ending_point):
        self.width = width
        self.height = height
        self.starting_point = starting_point
        self.ending_point = ending_point

    def generate_input(self):
        image = create_empty(self.height, self.width)
        image = create_frame_rectangle(image, self.starting_point, self.ending_point, SOLUTION_COLOR)

        image = create_dot(image, self.starting_point[0] + 1, self.starting_point[1] + 1, get_template_color(1))
        image = create_dot(image, self.ending_point[0] - 1, self.starting_point[1] + 1, get_template_color(2))
        image = create_dot(image, self.ending_point[0] - 1, self.ending_point[1] - 1, get_template_color(3))
        image = create_dot(image, self.starting_point[0] + 1, self.ending_point[1] - 1, get_template_color(4))

        return image

    def generate_output(self):
        image = create_empty(self.height, self.width)
        image = create_frame_rectangle(image, self.starting_point, self.ending_point, SOLUTION_COLOR)

        image = create_dot(image, self.starting_point[0] - 1, self.starting_point[1] - 1, get_template_color(1))
        image = create_dot(image, self.ending_point[0] + 1, self.starting_point[1] - 1, get_template_color(2))
        image = create_dot(image, self.ending_point[0] + 1, self.ending_point[1] + 1, get_template_color(3))
        image = create_dot(image, self.starting_point[0] - 1, self.ending_point[1] + 1, get_template_color(4))
        return image


class InsideOutsideSquareDotsVariationsGenerator:

    def generate_all(self):
        possible_values = []

        for height in range(6, 12):
            for width in range(6, 12):


                for start_x in range(1, width - 1):
                    for start_y in range(1, height - 1):
                        for end_x in range(start_x + 2, width - 1):
                            for end_y in range(start_y + 2, height - 1):

                                if not self.are_points_valid(start_x, start_y, end_x, end_y):
                                    continue

                                generator = InsideOutsideSquareDotsGenerator(width=width,
                                                                             height=height,
                                                                             starting_point=(start_y, start_x),
                                                                             ending_point=(end_y, end_x))
                                possible_values.append(generator)

        return possible_values


    def are_points_valid(self, start_x, start_y, end_x, end_y):
        if end_x - start_x < 3 or end_y - start_y < 3:
            return False

        return True
