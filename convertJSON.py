import os
import json

dir_list = os.listdir()

for dir_name in dir_list :

    try:

        with open(f'{dir_name}'+'/'+'AppImageInfo.json') as f:
            data = json.load(f)

    except :
        print(f"Skipped '{dir_name} folder' - does not have 'AppImageInfo.json' ")
        print("------------------------------------")

    try:
        results_sub_dir = os.getcwd() + '/results/' + f'{data["id"]}'

        new_data = {
            "file" : {
                "version" : data['file']['architecture'],
                "sha512checksum" : data['file']['sha512checksum'],
                "size" : data['file']['size'],
                "type" : data['file']['type'],
                "referring_url" : data['file']['url'],
                "id" : data['id'],
                "location" : results_sub_dir + '/AppImageInfo' + '.json',
            },
            "release" :
                {"date" : data['release']['date']},
            }

        if not os.path.exists(results_sub_dir):
            os.makedirs(results_sub_dir)

        with open('results/'  + f'{data["id"]}/' + 'AppImageInfo' + '.json', 'w') as json_file:
            json.dump(new_data, json_file, indent = 2)

    except Exception as e:
        print("Error folder name is :",dir_name)
        print("The Error is :",repr(e))
        print("------------------------------------")
