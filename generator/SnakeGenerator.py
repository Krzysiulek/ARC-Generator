from combinations.combinationcolor import SOLUTION_COLOR
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty, create_dot


class SnakeGenerator(GeneratorInterface):
    def __init__(self,
                 width,
                 height):
        self.width = width
        self.height = height

    def generate_input(self):
        image = create_empty(self.height, self.width)

        return image

    def generate_output(self):
        image = create_empty(self.height, self.width)

        right = True
        starting = 0

        for h in reversed(range(0, self.height)):
            create_dot(image, h, starting, SOLUTION_COLOR)

            if starting + 1 == self.width:
                right = False
            if starting == 0:
                right = True

            if right:
                starting += 1
            else:
                starting -= 1

        return image


class SnakeVariationsGenerator:

    def generate_all(self):
        possible_values = []

        for height in range(3, 30):
            for width in range(3, 30):
                if width > height:
                    continue

                generator = SnakeGenerator(width=width,
                                           height=height)
                possible_values.append(generator)

        return possible_values
