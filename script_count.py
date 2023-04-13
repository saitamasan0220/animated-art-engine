import os, re, glob
from random import shuffle

import random


# table = {}
# path='build/json/'
# for filename in os.listdir(path):
#     print(f'saving {filename} in table')
#     with open(path+filename, 'r') as file:
#         file_text = file.read()
#         table[filename] = file_text

indexes = list(range(1, 11989))

# count = 0
with os.scandir('build/json/') as directory:
    for item in directory:
        if item.is_file():
            index = item.name.replace(".json", "")
            int_index = int(index)
            print("index: ", int_index)
            indexes.remove(int_index)
            print("# remaining indexes: ", len(indexes))
            # count += 1 
    
print("remaining indexes: ", indexes)
print("# remaining indexes: ", len(indexes))
# print("count: ", count)
