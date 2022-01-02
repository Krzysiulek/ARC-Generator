import random

from generator.cropSmallestGenerator import CropSmallestVariationsGenerator
from json_formatter import JsonFormatter

# generator do wyboru
generator = CropSmallestVariationsGenerator()
N = 5
folder_to_save = 'data/crop_smallest/'


different_csgs = []
all_csg = generator.generate_all()
formatter = JsonFormatter()


# generuje problemy - templatki
for i, val in enumerate(all_csg):
    pairs = formatter.generate_problem_pairs(val, max=2)
    different_csgs.extend(pairs)

# tworzy indexy do wylosowania
problems_len = len(different_csgs)
random_indexes = random.sample(range(problems_len), problems_len)
random_indexes_sub_list = [random_indexes[n:n+N] for n in range(0, len(random_indexes), N)]

# zapisuje pliki po N losowych problemów
for i, val in enumerate(random_indexes_sub_list):
    random_problems_list = []

    for problem_indexes in val:
        random_problems_list.append(different_csgs[problem_indexes])

    file = folder_to_save + str(i) + '_cs.json'
    formatter.save_pairs_to_one_file(random_problems_list, file_name=file)
