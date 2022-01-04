# todo obsługa poleceń + help


# generator = CropSmallestVariationsGenerator()
from generator.cropSmallestGenerator import CropSmallestVariationsGenerator
from generator.frameGenerator import FrameVariationsGenerator
from generator.gravity2 import Gravity2VariationsGenerator
from generator.gravityGenerator import GravityVariationsGenerator
from run_generator import generate_and_save
from tqdm import tqdm

def run_crop_smallest():
    generate_and_save(generator=CropSmallestVariationsGenerator(),
                      N=5,
                      max_combinations_of_problem=5,
                      folder_to_save='data/crop_smallest',
                      values_to_insert=None,
                      short_problem_name='cs',
                      file_start_index=0)


def run_frame():
    last_index = 0

    for i in range(1, 9):
        last_index += generate_and_save(generator=FrameVariationsGenerator(),
                          N=5,
                          max_combinations_of_problem=5,
                          folder_to_save='data/frame',
                          values_to_insert=[i],
                          short_problem_name='frm',
                          file_start_index=last_index)


def run_gravity():
    generate_and_save(generator=Gravity2VariationsGenerator(),
                      N=5,
                      max_combinations_of_problem=5,
                      folder_to_save='data/gravity',
                      values_to_insert=None,
                      short_problem_name='grv',
                      file_start_index=0)


# run_frame()
# run_crop_smallest()
run_gravity()