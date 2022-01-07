from combinations.combinationcolor import SOLUTION_COLOR
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty, create_frame


class FrameGenerator(GeneratorInterface):
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
        image = create_frame(image, SOLUTION_COLOR)
        return image


class FrameVariationsGenerator:

    def generate_all(self):
        possible_values = []

        heights = [3, 4, 5, 6, 7, 8]
        widths = [3, 4, 5, 6, 7, 8]

        for height in heights:
            for width in widths:
                csg = FrameGenerator(width=width,
                                    height=height)
                possible_values.append(csg)

        return possible_values
