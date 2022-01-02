import numpy as np

from itertools import product, chain


class GravityGenerator:
    @staticmethod
    def generate_input(*, height, width):
        all_possible_zero_one_inputs = list(map(np.array, list(product([0, 1], repeat=height))))
        filtered_list_without_fully_filled = [item for item in all_possible_zero_one_inputs if sum(item) < height]
        all_possible_combinations = list(map(np.array, list(product(filtered_list_without_fully_filled, repeat=width))))
        all_possible_combinations_numpy = [item.T
                                           for item in all_possible_combinations
                                           if sum(chain(*item)) > 0]

        for single_array in all_possible_combinations_numpy[-10:]:
            result = np.where(single_array == 1)
            list_of_coordinates = list(zip(result[0], result[1]))
            temp_array = single_array.astype(dtype=np.chararray)
            for cords in list_of_coordinates:
                temp_array[cords] = f"SOLUTION_COLOR_{cords[1]}"
            yield temp_array

    @staticmethod
    def generate_output(image):
        height_values = np.count_nonzero(image, axis=0)
        uniques = np.unique((image[np.where(image != 0)]).astype("<U22"), axis=0)
        output = np.zeros(image.shape, dtype=np.chararray)
        for ix, _h in enumerate(height_values):
            output[4 - _h:, ix] = uniques[ix]
        return output
