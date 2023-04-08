import glob
import os

print('hello')
# Searching pattern inside folders and sub folders recursively
# search all jpg files
pattern = r"/Volumes/Extreme Pro/animated-art-engine/**/._*"

# pattern = r"/Volumes/Extreme Pro/**[MConverter.eu]*"

# pattern = r"E:\demos\files\reports\**\*.jpg"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting: ", item)
    os.remove(item)
    # print(item)

# Uncomment the below code check the remaining files
# print(glob.glob(r"E:\demos\files_demos\reports\**\*.*", recursive=True))