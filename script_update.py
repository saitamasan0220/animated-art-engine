import os
import re


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
