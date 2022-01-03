import itertools
from collections import Counter

import numpy as np


class MatrixValuesCombinationsError(BaseException):
    pass


class MatrixValuesCombinations:
    def __init__(self, matrix_input, values_to_insert, matrix_output=None):
        unique_inputs = self._parse_matrix(matrix_input)
        unique_output = self._parse_matrix(matrix_output)

        unique_merged = unique_inputs + unique_output

        # self.matrix_template_values = self._parse_matrix(unique_merged)
        self.matrix_template_values = unique_merged
        self.matrix_values_to_insert = values_to_insert
        if len(self.matrix_values_to_insert) < len(self.matrix_template_values):
            raise MatrixValuesCombinationsError("Number of values to insert < template values")
        self.matrix_dict = self._create_dict_with_unified_values()

    def _parse_matrix(self, matrix):
        matrix[matrix == 0] = "0"
        unique_values_in_matrix = list(np.unique(matrix))

        if unique_values_in_matrix.__contains__("0"):
            unique_values_in_matrix.remove("0")
        return unique_values_in_matrix

    def _create_dict_with_unified_values(self):
        return {
            key: self.matrix_values_to_insert for key in self.matrix_template_values
        }

    def create_matrixes_from_template(self, input_image, output_image, combinations, max=None):
        matrixes = []

        for i, combination in enumerate(combinations):
            if max is not None and i > max:
                break

            input_image_replaced = self.replace_colors(input_image, combination)
            output_image_replaced = self.replace_colors(output_image, combination)

            matrixes.append((input_image_replaced.tolist(), output_image_replaced.tolist()))

        return matrixes


    def replace_colors(self, image, combination):
        image_copy = np.copy(image)
        image_copy[image_copy == "0"] = 0
        for key in combination:
            color_value = combination[key]
            image_copy[image_copy == key] = color_value

        return image_copy

    def _get_max_occurences_values(self, counter_dict):
        return max(Counter(counter_dict.values()).values())

    def get_possible_template_values(self):
        print(*self.matrix_dict.items())
        keys, values = zip(*self.matrix_dict.items())
        permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
        return [d for d in permutations_dicts if self._get_max_occurences_values(d) < 2]
