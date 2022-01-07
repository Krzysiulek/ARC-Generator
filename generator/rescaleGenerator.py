import numpy as np

from itertools import product, chain


class RescaleGenerator:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.size = width * height
        self.desired_chunk_size = np.ones((height, width), dtype=int)
        self.inputs = []
        self.outputs = []

    def generate_input(self):
        mask = ((np.arange(2 ** self.size)[:, None] & (1 << np.arange(self.size))) != 0)
        out = mask.astype(int).reshape(-1, self.height, self.width)
        for single_array in out:
            if single_array.sum() > 0:
                result = np.where(single_array == 1)
                list_of_coordinates = list(zip(result[0], result[1]))
                temp_array = single_array.astype(dtype=np.chararray)
                for cords in list_of_coordinates:
                    temp_array[cords] = f"SOLUTION_COLOR_{cords[1] * self.width + cords[0]}"
                self.inputs.append(temp_array)
        return self.inputs

    def generate_output(self):
        for image in self.inputs:
            output = np.kron(image, self.desired_chunk_size)
            self.outputs.append(output)
        return self.outputs


class RescaleVariationsGenerator:

    def generate_all(self):
        # heights = [4, 5, 6, 7, 8]
        # widths = [4, 5, 6, 7, 8]
        heights = [2]
        widths = [2]
        return [
            RescaleGenerator(width=w, height=h)
            for w in widths for h in heights
        ]
