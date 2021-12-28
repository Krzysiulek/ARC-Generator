from unittest import TestCase
from combinations.combinations import MatrixValuesCombinations
import numpy as np

class ExampleMatrices:
    M1 = np.array([
        ["0", "0", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
    ], dtype=np.chararray)

    M2 = np.array([
        ["0", "TEMPLATE_COLOR_1", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
    ], dtype=np.chararray)

    M3 = np.array([
        ["0", "0", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
    ], dtype=np.chararray)

    M4 = np.array([
        ["0", "TEMPLATE_COLOR_1", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
        ["0", "0", "0", "SOLUTION_COLOR"],
    ], dtype=np.chararray)

class TestMatrixValuesCombinations(TestCase):
    def setUp(self):
        self.mvc1 = MatrixValuesCombinations(matrix=ExampleMatrices.M1, values_to_insert=[1,2])
        self.mvc2 = MatrixValuesCombinations(matrix=ExampleMatrices.M2, values_to_insert=[1,2])
        self.mvc3 = MatrixValuesCombinations(matrix=ExampleMatrices.M2, values_to_insert=[1,2,3])

class TestMatrixValuesCombinationsInit(TestMatrixValuesCombinations):
    def test_unique_values(self):
        self.assertEqual(self.mvc1.matrix_template_values, ["SOLUTION_COLOR"])

class TestMatrixValuesCombinationsValues(TestMatrixValuesCombinations):
    def test_get_possible_template_values(self):
        self.assertEqual(self.mvc1.get_possible_template_values(),
                         [{'SOLUTION_COLOR': 1}, {'SOLUTION_COLOR': 2}])
        self.assertEqual(self.mvc2.get_possible_template_values(),
                         [{'SOLUTION_COLOR': 1, 'TEMPLATE_COLOR_1': 2}, {'SOLUTION_COLOR': 2, 'TEMPLATE_COLOR_1': 1}])
        self.assertEqual(self.mvc3.get_possible_template_values(),
                         [{'SOLUTION_COLOR': 1, 'TEMPLATE_COLOR_1': 2}, {'SOLUTION_COLOR': 1, 'TEMPLATE_COLOR_1': 3},
                          {'SOLUTION_COLOR': 2, 'TEMPLATE_COLOR_1': 1}, {'SOLUTION_COLOR': 2, 'TEMPLATE_COLOR_1': 3},
                          {'SOLUTION_COLOR': 3, 'TEMPLATE_COLOR_1': 1}, {'SOLUTION_COLOR': 3, 'TEMPLATE_COLOR_1': 2}]
                         )