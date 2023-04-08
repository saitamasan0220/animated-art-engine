import os, re, glob
from random import shuffle

import random



pattern = r"./build/**/.DS_Store"

for item in glob.iglob(pattern, recursive=True):
    print("Deleting: ", item)
    os.remove(item)
    # print(item)


numNFTs = 12
shuffledIndexes = list(range(1, numNFTs+1))
shuffle(shuffledIndexes)
shuffledIndexes = [0] + shuffledIndexes

print("shuffledIndexes: ", shuffledIndexes)


table = {}

path='build/json/'
for filename in os.listdir(path):
    print(f'saving {filename} in table')
    with open(path+filename, 'r') as file:
        file_text = file.read()
        table[filename] = file_text

path='build/gif/'
for filename in (os.listdir(path)):
    shuffle_index = int(filename.replace('.gif', ''))
    swapped_file = str(shuffledIndexes[shuffle_index]) + '.gif'
    print(f'{filename} switched with {swapped_file}')
    my_source = path + filename
    my_dest  = path + f'{shuffledIndexes[shuffle_index]}.temp.gif'
    os.rename(my_source, my_dest) # switch A to B
    print(f'{my_source} renamed to {my_dest}\n')

for filename in os.listdir(path):
    my_source = path + filename
    my_dest  = path + filename.replace('.temp.gif', '.gif')
    os.rename(my_source, my_dest)


path='build/json/'
for filename in os.listdir(path):
    table_key = int(filename.replace('.json', ''))
    my_source = path + filename
    my_dest  = path + f'{shuffledIndexes[table_key]}.temp.json'
    os.rename(my_source, my_dest)

for filename in os.listdir(path):
    my_source = path + filename
    my_dest  = path + filename.replace('.temp.json', '.json')
    os.rename(my_source, my_dest)


with os.scandir('build/json/') as directory:
    for item in directory:
        for i in range(numNFTs):
            if item.is_file():

                # correct gif names in metadata
                with open(item, mode="r+") as file:

                    file_text = file.read()
                    regex = re.compile('\d+.gif')
                    new_name = item.name.replace('.json', '.gif')
                    file_text = regex.sub(f'{new_name}', file_text)
                    file.seek(0)
                    file.write(file_text)
