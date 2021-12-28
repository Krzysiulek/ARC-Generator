import io
import json

# a Python object (dict):
from generator.cropSmallestGenerator import CropSmallestGenerator

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)


# the result is a JSON string:

class JsonFormatter:

    def generate_problem_pair(self):
        cropSmallest = CropSmallestGenerator(width=4,
                                             height=5,
                                             smallest_position=(1, 2),
                                             smallest_size=2)
        input_array = cropSmallest.generate_input()
        output_array = cropSmallest.generate_output()

        return {
            "input": input_array,
            "output": output_array
        }

    def generate_crop_smallest(self):
        problem_pair = self.generate_problem_pair()

        info = {
            "train": [
                problem_pair
            ],
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

        print(info)
        y = json.dumps(info)
        print(y)

        with io.open('data.json', 'w', encoding='utf-8') as f:
            f.write(y)


JsonFormatter().generate_crop_smallest()
