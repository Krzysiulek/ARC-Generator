from combinations.combinationcolor import SOLUTION_COLOR
from generator.generatorInteface import GeneratorInterface
from utils.shapesGenerator import create_empty


class TwistedCrossGenerator(GeneratorInterface):
    def __init__(self,
                 side_len):
        self.side_len = side_len

    def generate_input(self):
        image = create_empty(self.side_len, self.side_len)
        image[image == 0] = SOLUTION_COLOR

        midfield_id = int((self.side_len - 1) / 2)

        image[midfield_id][midfield_id] = 0

        return image

    def generate_output(self):
        image = create_empty(self.side_len, self.side_len)
        image[image == 0] = SOLUTION_COLOR

        for i in range(0, self.side_len):
            image[i][i] = 0

            reversed_i = self.side_len - i - 1
            image[i][reversed_i] = 0

        return image


class TwistedCrossVariationsGenerator:

    def generate_all(self):
        possible_values = []

        for side_len in range(3, 33):
            if side_len % 2 == 0:
                continue

            generator = TwistedCrossGenerator(side_len=side_len)
            possible_values.append(generator)

        return possible_values

