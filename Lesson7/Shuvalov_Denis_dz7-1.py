import os

p_list = {'my_proj': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, value in p_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))