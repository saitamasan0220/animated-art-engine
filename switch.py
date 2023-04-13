import sys
import os
import re
import glob
from random import shuffle

import random

# random_indexes = random.sample(range(1, 11989), 12)
# # random_indexes = [0] + random_indexes

# random_map = {}
# for random_index in random_indexes:
#     for ascended_index in range(11989, 12001):
#         random_map[random_index] = ascended_index
#         random_map[ascended_index] = random_index

# for i, arg in enumerate(sys.argv):
#     print(f"Argument {i:>6}: {arg}")


arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

random_map = {
    arg1: arg2,
    arg2: arg1
}


path = 'build/random/gif/'
for filename in (os.listdir(path)):
    map_index = int(filename.replace('.gif', ''))
    if map_index in random_map:
        swapped_file = str(random_map[map_index]) + '.gif'
        print(f'{filename} switched with {swapped_file}')
        my_source = path + filename
        my_dest = path + f'{random_map[map_index]}.temp.gif'
        os.rename(my_source, my_dest)  # switch A to B
        print(f'{my_source} renamed to {my_dest}\n')

for filename in os.listdir(path):
    my_source = path + filename
    my_dest = path + filename.replace('.temp.gif', '.gif')
    os.rename(my_source, my_dest)


path = 'build/random/json/'
for filename in os.listdir(path):
    map_index = int(filename.replace('.json', ''))
    if map_index in random_map:
        my_source = path + filename
        my_dest = path + f'{random_map[map_index]}.temp.json'
        os.rename(my_source, my_dest)

for filename in os.listdir(path):
    my_source = path + filename
    my_dest = path + filename.replace('.temp.json', '.json')
    os.rename(my_source, my_dest)


with os.scandir('build/random/json/') as directory:
    for item in directory:
        if item.is_file():
            with open(item, mode="r+") as file:

                file_text = file.read()
                regex = re.compile('\d+.gif')
                new_name = item.name.replace('.json', '.gif')
                file_text = regex.sub(f'{new_name}', file_text)
                file.seek(0)
                file.write(file_text)
