import os
import re
import glob
from random import shuffle

import random

# random_indexes = random.sample(range(1, 11989), 11)
# random_map = {}
# i = 0
# for ascended_index in range(11989, 12000):
#     random_index = random_indexes[i]
#     i += 1
#     random_map[random_index] = ascended_index
#     random_map[ascended_index] = random_index

# print("random_indexes: ", random_indexes)
# print("random_map: ", random_map)

# path = 'build/gif/'
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


# path = 'build/json/'
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

random_map = {9833: 11989, 11989: 9833, 6357: 11990, 11990: 6357, 1461: 11991, 11991: 1461, 8951: 11992, 11992: 8951, 633: 11993, 11993: 633, 6477: 11994,
              11994: 6477, 6879: 11995, 11995: 6879, 9386: 11996, 11996: 9386, 8897: 11997, 11997: 8897, 1697: 11998, 11998: 1697, 11119: 11999, 11999: 11119}


with os.scandir('build/json/') as directory:
    for item in directory:
        if item.is_file() and int(item.name.replace('.json', '')) in random_map:
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
                file.close()

print("done")
