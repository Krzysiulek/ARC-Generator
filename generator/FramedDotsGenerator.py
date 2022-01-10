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
            image = create_dot(image, dot[0] - 1, dot[1], get_template_color(1))
            image = create_dot(image, dot[0] + 1, dot[1], get_template_color(1))
            image = create_dot(image, dot[0] + 1, dot[1] + 1, get_template_color(1))
            image = create_dot(image, dot[0] - 1, dot[1] + 1, get_template_color(1))
            image = create_dot(image, dot[0], dot[1] + 1, get_template_color(1))
            image = create_dot(image, dot[0], dot[1] - 1, get_template_color(1))
            image = create_dot(image, dot[0] + 1, dot[1] - 1, get_template_color(1))
            image = create_dot(image, dot[0] - 1, dot[1] - 1, get_template_color(1))

        return image

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

                # if width != height:
                #     continue

                max_dots_number = 5
                dots = self.get_dots_positions_combinations(height - 3, width - 3, max_dots_number)

                for dots_combinations in dots:
                    generator = FramedDotsGenerator(width=width,
                                                   height=height,
                                                    dots_positions=dots_combinations)
                    possible_values.append(generator)

        return possible_values


    def get_dots_positions_combinations(self, height, width, dots_number):
        all_dots = []
        dots_to_return = []

        for h in range(1, height):
            for w in range(1, width):
                all_dots.append((h, w))

        for dot_idx in range(0, len(all_dots) - dots_number - 1):
            tmp_dots = []

            for i in range(1, dots_number):


                iterat = 0
                while (iterat < len(all_dots) - iterat):
                    iterat+=1

                    if len(tmp_dots) >= i:
                        break

                    if (dot_idx + iterat) >= len(all_dots):
                        break

                    dot = all_dots[dot_idx + iterat]

                    if (self.is_such_dot_possible(dot[0], dot[1], tmp_dots, height, width)):
                        tmp_dots.append((dot[0], dot[1]))


                if len(tmp_dots) == i - 1:
                    dots_to_return.append(tmp_dots)

        return dots_to_return

    def is_such_dot_possible(self, height_point, width_point, tmp_dots, image_height, image_width):

        for dot in tmp_dots:

            if dot[0] >= image_height:
                return False

            if dot[1] >= image_width:
                return False

            space_between = 2

            if dot[0] - space_between <= height_point <= dot[0] + space_between:
                return False

            if dot[1] - space_between <= width_point <= dot[1] + space_between:
                return False

        return True





