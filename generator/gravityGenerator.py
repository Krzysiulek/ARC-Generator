import numpy as np

from itertools import product, chain


# Pozwoliłem sobie przenieść ten problem do pliku gravity2.py, żeby był bardziej przystosowany do tego mechanizmu, który aktualnie mamy
from combinations.combinationcolor import get_template_color


class GravityGenerator:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.inputs = []
        self.outputs = []

    def generate_input(self):
        all_possible_zero_one_inputs = list(map(np.array, list(product([0, 1], repeat=self.height))))
        filtered_list_without_fully_filled = [item for item in all_possible_zero_one_inputs if sum(item) < self.height]
        all_possible_combinations = list(
            map(np.array, list(product(filtered_list_without_fully_filled, repeat=self.width))))
        all_possible_combinations_numpy = [item.T
                                           for item in all_possible_combinations
                                           if sum(chain(*item)) > 0]

        for single_array in all_possible_combinations_numpy:
            result = np.where(single_array == 1)
            list_of_coordinates = list(zip(result[0], result[1]))
            temp_array = single_array.astype(dtype=np.chararray)
            for cords in list_of_coordinates:
                temp_array[cords] = get_template_color(cords[1])
            self.inputs.append(temp_array)
        return np.array(self.inputs)

    def generate_output(self):
        for image in self.inputs:
            height_values = np.count_nonzero(image, axis=0)
            uniques = np.unique((image[np.where(image != 0)]).astype("<U22"), axis=0)
            output = np.zeros(image.shape, dtype=np.chararray)
            ix = 0
            for _w, _h in enumerate(height_values):
                if _h != 0:
                    output[self.height - _h:, _w] = uniques[ix]
                    ix += 1
            self.outputs.append(output)
        return np.array(self.outputs)


class GravityVariationsGenerator:

    def generate_all(self):
        # heights = [4, 5, 6, 7, 8]
        heights = [4]
        widths = [4]
        # widths = [4, 5, 6, 7, 8]

        return [
            GravityGenerator(width=w, height=h)
            for w in widths for h in heights
        ]
