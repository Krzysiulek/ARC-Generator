import io
import json

# a Python object (dict):
from combinations.combinations import MatrixValuesCombinations
from generator.cropSmallestGenerator import CropSmallestGenerator, CropSmallestModel, CropSmallestVariationsGenerator
import random


class JsonFormatter:
    # iter tools, combinations

    def generate_problem_pairs(self, problem, max=None):
        input_array = problem.generate_input()
        output_array = problem.generate_output()

        mvc = MatrixValuesCombinations(matrix=input_array, values_to_insert=[1, 2, 3, 4, 5, 6, 7, 8])
        possible_values = mvc.get_possible_template_values()
        input_combinations = mvc.create_matrixes_from_template(input_array, output_array, possible_values, max)

        pairs = []
        for combination in input_combinations:
            pairs.append({
                "input": combination[0],
                "output": combination[1]
            })

        return pairs


    def save_pairs_to_one_file(self, problems, file_name):
        train_pairs = problems[1:]
        test_pair = [problems[0]]

        info = {
            "train": train_pairs,
            "test": test_pair
        }

        y = json.dumps(info)
        with io.open(file_name, 'w', encoding='utf-8') as f:
            f.write(y)


    def save_to_file(self, file_name='data.json', csg=None):
        problem_pairs = self.generate_problem_pairs(csg, max=4)

        # train_pairs =
        # test_pair = pro

        info = {
            "train": problem_pairs,
            "test": [
                {
                    "input": [
                        [0]
                    ],
                    "output": [
                        [0]
                    ]
                }
            ]
        }

        y = json.dumps(info)
        with io.open(file_name, 'w', encoding='utf-8') as f:
            f.write(y)


