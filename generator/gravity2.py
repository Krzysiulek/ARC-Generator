from itertools import product, chain

import numpy as np

from combinations.combinationcolor import get_template_color
from generator.generatorInteface import GeneratorInterface
from tqdm import tqdm


class Gravity2Generator(GeneratorInterface):

    def __init__(self, height, width, singe_array):
        self.height = height
        self.width = width
        self.single_array = singe_array
        self.input = None

    def generate_input(self):
        result = np.where(self.single_array == 1)
        list_of_coordinates = list(zip(result[0], result[1]))
        temp_array = self.single_array.astype(dtype=np.chararray)
        for cords in list_of_coordinates:
            temp_array[cords] = get_template_color(cords[1])


        self.input = temp_array
        return np.array(temp_array)

    def generate_output(self):
        image = self.input

        height_values = np.count_nonzero(image, axis=0)
        uniques = np.unique((image[np.where(image != 0)]).astype("<U22"), axis=0)
        output = np.zeros(image.shape, dtype=np.chararray)
        ix = 0
        for _w, _h in enumerate(height_values):
            if _h != 0:
                output[self.height - _h:, _w] = uniques[ix]
                ix += 1

        return np.array(output)


class Gravity2VariationsGenerator:

    def generate_all(self):
        all_possibilities = []

        heights = [4]
        widths = [4]

        for height in tqdm(heights, desc='height', position=0):
            for width in tqdm(widths, desc='width', position=1, leave=False):

                all_possible_zero_one_inputs = list(map(np.array, list(product([0, 1], repeat=height))))
                filtered_list_without_fully_filled = [item for item in all_possible_zero_one_inputs if
                                                      sum(item) < height]
                all_possible_combinations = list(
                    map(np.array, list(product(filtered_list_without_fully_filled, repeat=width))))
                all_possible_combinations_numpy = [item.T
                                                   for item in all_possible_combinations
                                                   if sum(chain(*item)) > 0]

                for single_array in all_possible_combinations_numpy:
                    all_possibilities.append(Gravity2Generator(height=height, width=width, singe_array=single_array))

        return all_possibilities
