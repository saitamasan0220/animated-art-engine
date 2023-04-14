import os
import re


with os.scandir('build/json/') as directory:
    for item in directory:
        if item.is_file():
            with open(item, mode="r+") as file:

                file_text = file.read()

                # regex = re.compile('WEBUriToReplace')
                # new_text_uri = 'QmZ8uTmkNaQ9yePkUcc7KKoSc2rtWMjYW3rgc2oCmAxYSo'
                # file_text = regex.sub(f'{new_text_uri}', file_text)

                # id = int(item.name.replace('.json', ''))

                # regex = re.compile('NewUriToReplace')

                # if 1 <= id <= 3000:  # q1
                #     new_folder_uri = 'QmTVHvsZj1kM3szmm7SvyNqAAmfKVTaXjyV9GBhVBbdXEU'
                #     print("new_folder_uri: ", new_folder_uri)
                # elif 3001 <= id <= 6000:  # q2
                #     new_folder_uri = 'QmTYK7igKqx7oLKtdLWJbB9BwCGDLYH653mL8GFs1MRtgM'
                #     print("new_folder_uri: ", new_folder_uri)
                # elif 6001 <= id <= 9000:  # q3
                #     new_folder_uri = 'QmeMo7rFzgKFAGu2DR7uC5tn9PPURfKf2A3goXnHAgxBns'
                #     print("new_folder_uri: ", new_folder_uri)
                # else:  # q4
                #     new_folder_uri = 'QmTurjANBZboTdQzGepW6zTjcoyxULEYymcE3bstWMPPoy'
                #     print("new_folder_uri: ", new_folder_uri)
                # file_text = regex.sub(f'{new_folder_uri}', file_text)

                # regex = re.compile(']')
                # fee_data = '], \n\t"seller_fee_basis_points": 1000, \n\t"fee_recipient": "0x796e1fC022dAbcCf0066488A6Ed1e0e7400Af1d3"'
                # file_text = regex.sub(f'{fee_data}', file_text)

                file.seek(0)
                file.write(file_text)
                file.close()

print("done")
