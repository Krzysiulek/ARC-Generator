import numpy as np
from numpy import int64

from utils.shapesGenerator import square_generator


class CropSmallestGenerator:

    def __init__(self,
                 width,
                 height,
                 smallest_position,
                 smallest_size):
        self.width = width
        self.height = height

        self.smallest_position = smallest_position
        self.smallest_size = smallest_size
        self.bigger_amount = 3
        self.smallest_color = 1


    def generate_input(self):
        size = (self.height, self.width)
        image = np.zeros(size, dtype=np.chararray)

        for _ in range(self.bigger_amount):
            # todo generowanie większych
            image = square_generator(image, self.smallest_position, self.smallest_size, self.smallest_color)

        image = square_generator(image, self.smallest_position, self.smallest_size, "SOL_COL")

        return image.tolist()

    def generate_output(self):
        image = np.full((self.smallest_size, self.smallest_size), self.smallest_color)
        return image.tolist()
