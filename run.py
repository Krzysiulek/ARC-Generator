# todo obsługa poleceń + help


# generator = CropSmallestVariationsGenerator()
from generator.FramedDotsGenerator import FramedDotsVariationsGenerator
from generator.SnakeGenerator import SnakeVariationsGenerator
from generator.TwistedCrossGenerator import TwistedCrossVariationsGenerator
from generator.cropSmallestGenerator import CropSmallestVariationsGenerator
from generator.frameGenerator import FrameVariationsGenerator
from generator.gravity2 import Gravity2VariationsGenerator
from generator.labyrinthGenerator import LabyrinthVariationsGenerator
from generator.repetitionGenerator import RepetitionVariationsGenerator
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
                                        max_combinations_of_problem=None,
                                        folder_to_save='data/frame',
                                        values_to_insert=[i],
                                        short_problem_name='frm',
                                        file_start_index=last_index)


def run_gravity():
    generate_and_save(generator=Gravity2VariationsGenerator(),
                      N=5,
                      max_combinations_of_problem=5,
                      folder_to_save='data/inputs/gravity/5',
                      values_to_insert=None,
                      short_problem_name='grv',
                      file_start_index=0)


def run_snake():
    last_index = 0

    for i in range(1, 10):
        last_index += generate_and_save(generator=SnakeVariationsGenerator(),
                                        N=20,
                                        max_combinations_of_problem=None,
                                        folder_to_save='data/inputs/snake/20',
                                        values_to_insert=[i],
                                        short_problem_name='snk',
                                        file_start_index=last_index)


def run_repetition():
    generate_and_save(generator=RepetitionVariationsGenerator(),
                      N=5,
                      max_combinations_of_problem=None,
                      folder_to_save='data/inputs/repetition',
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

def run_labyrinth():
    last_index = 0

    for i in range(1, 10):
        last_index += generate_and_save(generator=LabyrinthVariationsGenerator(),
                          N=20,
                          max_combinations_of_problem=None,
                          folder_to_save='data/inputs/labyrinth2/20',
                          values_to_insert=[i],
                          short_problem_name='lab',
                          file_start_index=last_index,
                          solution_color_sticked_value=i)


def run_framed_dots():
    last_index = 0

    for i in range(1, 9):
        last_index += generate_and_save(generator=FramedDotsVariationsGenerator(),
                      N=30,
                      max_combinations_of_problem=None,
                      folder_to_save='data/inputs/framed_dots/30',
                      values_to_insert=[i, i+1],
                      short_problem_name='frm-dot',
                      file_start_index=last_index,
                      solution_color_sticked_value=i)


def run_twisted_cross():
    generate_and_save(generator=TwistedCrossVariationsGenerator(),
                                        N=5,
                                        max_combinations_of_problem=None,
                                        folder_to_save='data/inputs/twised_cross/5',
                                        values_to_insert=[1,2,3,4,5,6,7,8,9],
                                        short_problem_name='tws-crs',
                                        file_start_index=0,
                                        solution_color_sticked_value=None)

# run_frame() # done
# run_crop_smallest() # tego nie robimy, bo input.size != output.size
# run_gravity() # to na później, bo się długo generuje
# run_snake()
# run_repetition()
# run_rescale()
# run_labyrinth()
# run_framed_dots()
run_twisted_cross()


# FRAME:
# 5x100
# 10x100
# 30x100
# 50x100
# 100x100?