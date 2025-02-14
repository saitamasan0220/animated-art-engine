import os
import re
import glob
from random import shuffle

import random

# random_indexes = [6869, 10340, 11019]

# random_map = {}
# for random_index in random_indexes:
#     for ascended_index in range(1, 4):
#         random_map[random_index] = ascended_index
#         random_map[ascended_index] = random_index

# path = 'build-missing/random/gif/'
# for filename in (os.listdir(path)):
#     map_index = int(filename.replace('.gif', ''))
#     if map_index in random_map:
#         swapped_file = str(random_map[map_index]) + '.gif'
#         print(f'{filename} switched with {swapped_file}')
#         my_source = path + filename
#         my_dest = path + f'{random_map[map_index]}.temp.gif'
#         os.rename(my_source, my_dest)  # switch A to B
#         print(f'{my_source} renamed to {my_dest}\n')

# for filename in os.listdir(path):
#     my_source = path + filename
#     my_dest = path + filename.replace('.temp.gif', '.gif')
#     os.rename(my_source, my_dest)


# path = 'build-missing/random/json/'
# for filename in os.listdir(path):
#     map_index = int(filename.replace('.json', ''))
#     if map_index in random_map:
#         my_source = path + filename
#         my_dest = path + f'{random_map[map_index]}.temp.json'
#         os.rename(my_source, my_dest)

# for filename in os.listdir(path):
#     my_source = path + filename
#     my_dest = path + filename.replace('.temp.json', '.json')
#     os.rename(my_source, my_dest)


with os.scandir('build-missing/json/') as directory:
    for item in directory:
        if item.is_file():
            with open(item, mode="r+") as file:

                file_text = file.read()

                regex = re.compile('\d+.gif')
                new_name = item.name.replace('.json', '.gif')
                file_text = regex.sub(f'{new_name}', file_text)

                regex = re.compile('#\d+')
                new_name = '#' + item.name.replace('.json', '')
                file_text = regex.sub(f'{new_name}', file_text)

                file.seek(0)
                file.write(file_text)
