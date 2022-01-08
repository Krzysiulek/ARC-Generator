# todo obsługa poleceń + help


# generator = CropSmallestVariationsGenerator()
from generator.SnakeGenerator import SnakeVariationsGenerator
from generator.cropSmallestGenerator import CropSmallestVariationsGenerator
from generator.frameGenerator import FrameVariationsGenerator
from generator.gravity2 import Gravity2VariationsGenerator
from generator.repetitionGenerator import RepetitionVariationsGenerator
from generator.rescaleGenerator import RescaleVariationsGenerator
from generator.resize2 import ResizeVariationsGenerator
from run_generator import generate_and_save


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

    for i in range(1, 10):
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


def run_snake():
    last_index = 0

    for i in range(1, 10):
        last_index += generate_and_save(generator=SnakeVariationsGenerator(),
                                        N=5,
                                        max_combinations_of_problem=None,
                                        folder_to_save='data/snake',
                                        values_to_insert=[i],
                                        short_problem_name='snk',
                                        file_start_index=last_index)


def run_repetition():
    generate_and_save(generator=RepetitionVariationsGenerator(),
                      N=5,
                      max_combinations_of_problem=None,
                      folder_to_save='data/repetition',
                      values_to_insert=[1,2],
                      short_problem_name='rep',
                      file_start_index=0,
                      solution_color_sticked_value=2)

def run_rescale():
    generate_and_save(generator=ResizeVariationsGenerator(),
                      N=5,
                      max_combinations_of_problem=None,
                      folder_to_save='data/resize',
                      values_to_insert=None,
                      short_problem_name='res',
                      file_start_index=0,
                      solution_color_sticked_value=0)



# run_frame()
# run_crop_smallest()
# run_gravity()
# run_snake()
# run_repetition()
run_rescale()