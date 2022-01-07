import random
import os

from tqdm import tqdm

from generator.cropSmallestGenerator import CropSmallestVariationsGenerator
from generator.frameGenerator import FrameVariationsGenerator
from json_formatter import JsonFormatter

# generator do wyboru
# generator = CropSmallestVariationsGenerator()
generator = FrameVariationsGenerator()
N = 5
MAX_COMBINATIONS_OF_PROBLEM = 5  # ile wariacji koloru dla jednego problemu. Dla None generuje maksymalnie dużo kombinacji

# todo przenieść to do generatora
folder_to_save = 'data/frame/'

def generate_and_save(generator,
                      N,
                      max_combinations_of_problem,
                      folder_to_save,
                      values_to_insert,
                      short_problem_name='',
                      file_start_index=0,
                      solution_color_sticked_value=None):
    different_csgs = []
    all_csg = generator.generate_all()
    formatter = JsonFormatter()

    # generuje problemy - templatki
    for i, val in tqdm(enumerate(all_csg), total=len(all_csg), desc="Generowanie templatek"):
        pairs = formatter.generate_problem_pairs(val,
                                                 max=max_combinations_of_problem,
                                                 values_to_insert=values_to_insert,
                                                 solution_color_sticked_value=solution_color_sticked_value)
        different_csgs.extend(pairs)

    # tworzy indexy do wylosowania
    problems_len = len(different_csgs)
    random_indexes = random.sample(range(problems_len), problems_len)
    random_indexes_sub_list = [random_indexes[n:n + N] for n in range(0, len(random_indexes), N)]

    # zapisuje pliki po N losowych problemów
    max_i = 0
    for i, val in tqdm(enumerate(random_indexes_sub_list), desc="Zapisywanie", total=len(random_indexes_sub_list)):
        random_problems_list = []
        max_i = i

        for problem_indexes in val:
            random_problems_list.append(different_csgs[problem_indexes])

        if len(random_problems_list) < N:
            print("Skipping")
            continue

        os.makedirs(folder_to_save, exist_ok = True)
        file = f"{folder_to_save}/{i+file_start_index}_{short_problem_name}.json"
        formatter.save_pairs_to_one_file(random_problems_list, file_name=file)

    return max_i