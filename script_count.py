import os, re, glob
from random import shuffle

import random



path='build/json/'
for filename in os.listdir(path):
    print(f'saving {filename} in table')
    with open(path+filename, 'r') as file:
        file_text = file.read()
        table[filename] = file_text

indexes = list(range(1, 19886))

with os.scandir('build/json/') as directory:
    for item in directory:
        if item.is_file():
            index = item.name.replace(".json", "")
            indexes.remove(index)
    
print("remaining indexes: ", indexes)
