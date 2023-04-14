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

# indexes = list(range(1, 11989))

# # count = 0
# with os.scandir('build/json/') as directory:
#     for item in directory:
#         if item.is_file():
#             index = item.name.replace(".json", "")
#             int_index = int(index)
#             # print("index: ", int_index)
#             indexes.remove(int_index)
#             # print("# remaining indexes: ", len(indexes))
#             # count += 1

# print("missing json: ", indexes)
# print("# remaining indexes: ", len(indexes))
# # print("count: ", count)

# # ###############################################################
# indexes = list(range(1, 11989))

# with os.scandir('build/gif/') as directory:
#     for item in directory:
#         if item.is_file():
#             index = item.name.replace(".gif", "")
#             int_index = int(index)
#             indexes.remove(int_index)

# print("missing gifs: ", indexes)
# print("# remaining indexes: ", len(indexes))
# # print("count: ", count)

# # #################################################

with open('./table.json', 'r') as f:
    table = json.load(f)


# def rec_dd(): return defaultdict(rec_dd)
# table = rec_dd()

path = 'build/json/'
for filename in os.listdir(path):
    # print(f'saving {filename} in table')
    with open(path+filename, 'r') as file:
        data = json.load(file)
        attributes = data["attributes"]

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

        # print("table[{}][{}][{}]: {}".format(Background, Bible, Verse,
        #                                          table[Background][Bible][Verse]))

        if Rarity == "Baptized":
            # print("table[{}][{}][{}][{}]: {}".format(Background, Bible, Cross, Verse,
            #                                          table[Background][Bible][Cross][Verse]))
            if table[Background][Bible][Cross][Verse]:

                # print("can't use {}".format(filename))
                print("", end='')
            else:
                print("can use {}".format(filename))

        elif Rarity == "Anointed":
            # print("table[{}][{}][{}]: {}".format(Background, Bible, Verse,
            #                                      table[Background][Bible][Verse]))
            # if table[Background][Bible][Verse]:
            #     print("", end='')
            #     # print("can't use {}".format(filename))
            # else:
            #     print("can use {}".format(filename))

            if Verse not in table[Background][Bible]:
                print("can use {}".format(filename))


print("done")
