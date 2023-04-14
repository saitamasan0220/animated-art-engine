import sys
import os
import re
import glob
from random import shuffle

import random

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

random_map = {
    arg1: arg2,
    arg2: arg1
}


path = 'ascended/gif/'
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


path = 'ascended/json/'
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


with os.scandir('ascended/json/') as directory:
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
