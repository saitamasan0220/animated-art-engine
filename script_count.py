from collections import defaultdict
import json
import os
import re
import glob
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
            # print("index: ", int_index)
            indexes.remove(int_index)
            # print("# remaining indexes: ", len(indexes))
            # count += 1

print("missing json: ", indexes)
print("# remaining indexes: ", len(indexes))
# print("count: ", count)

# ###############################################################
indexes = list(range(1, 11989))

with os.scandir('build/gif/') as directory:
    for item in directory:
        if item.is_file():
            index = item.name.replace(".gif", "")
            int_index = int(index)
            indexes.remove(int_index)

print("missing gifs: ", indexes)
print("# remaining indexes: ", len(indexes))
# print("count: ", count)

# #################################################


def rec_dd(): return defaultdict(rec_dd)


baptized_count = 0
anointed_count = 0

table = rec_dd()
path = 'build/json/'
for filename in os.listdir(path):
    # print(f'saving {filename} in table')
    with open(path+filename, 'r') as file:
        data = json.load(file)
        attributes = data["attributes"]
        '''
            {
            "trait_type": "Background",
            "value": "Eliashib"
            },
            {
            "trait_type": "Bible",
            "value": "Reuben"
            },
            {
            "trait_type": "Cross",
            "value": "Self Control"
            },
            {
            "trait_type": "Verse",
            "value": "Romans 6_23"
            },
            {
            "trait_type": "Rarity",
            "value": "Baptized"
            }
        '''
        for attribute in attributes:
            if attribute["trait_type"] == "Background":
                Background = attribute["value"]
            if attribute["trait_type"] == "Bible":
                Bible = attribute["value"]
            if attribute["trait_type"] == "Cross":
                Cross = attribute["value"]
            if attribute["trait_type"] == "Verse":
                Verse = attribute["value"]
            if attribute["trait_type"] == "Rarity":
                Rarity = attribute["value"]

        if Rarity == "Baptized":
            # table["Background"] = {
            #     "value": Background,
            #     "Bible": Bible,
            #     "Cross": Cross,
            #     "Verse": Verse
            # }
            table[Background][Bible][Cross][Verse] = True
            print("table[{}][{}][{}][{}]: {}".format(Background, Bible, Cross, Verse,
                                                     table[Background][Bible][Cross][Verse]))
            baptized_count += 1
        elif Rarity == "Anointed":
            # table["Background"] = {
            #     "value": Background,
            #     "Bible": Bible,
            #     "Verse": Verse
            # }
            table[Background][Bible][Verse] = True
            print("table[{}][{}][{}]: {}".format(Background, Bible, Verse,
                                                 table[Background][Bible][Verse]))
            anointed_count += 1


print("baptized_count: ", baptized_count)
print("anointed_count: ", anointed_count)

with open('table.json', 'w') as json_file:
    json.dump(table, json_file)

print("done")
