import os
import re
import glob
from random import shuffle

import random

indexes = list(range(1, 12001))

path = 'build/gif/'
for filename in (os.listdir(path)):
    map_index = int(filename.replace('.gif', ''))
    indexes.remove(map_index)

print("missing gif's: ", indexes)
