import os
import re


with os.scandir('build/json/') as directory:
    for item in directory:
        if item.is_file():
            with open(item, mode="r+") as file:

                file_text = file.read()

                regex = re.compile('WEBUriToReplace')
                new_text_uri =
                file_text = regex.sub(f'{new_text_uri}', file_text)

                id = int(item.name.replace('.json', ''))

                regex = re.compile('NewUriToReplace')

                if 1 <= id <= 3000:  # q1
                    new_folder_uri =
                elif 3001 <= id <= 6000:  # q2
                    new_folder_uri =
                elif 1 <= id <= 3000:  # q3
                    new_folder_uri =
                else:  # q4
                    new_folder_uri =
                file_text = regex.sub(f'{new_folder_uri}', file_text)

                print("new_folder_uri: ", new_folder_uri)

                file.seek(0)
                file.write(file_text)
                file.close()

print("done")
