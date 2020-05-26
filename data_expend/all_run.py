import os
import pathlib
import json

# os.system("python -m data_expend.dict_to_json")
os.system("python -m data_expend.json_to_conllx")
os.system("python -m data_expend.merge_data")

# read mapping
with open("./data/mapping.json", 'r', encoding='UTF-8') as f:
    map_list = json.load(f)

# path = pathlib.Path('./data/mapping.json')

# data expand
# if path.exists():
if map_list:
    os.system("python -m data_expend.meta_generator")
    os.system("python -m data_expend.generate_seq2")

os.system("python -m data_expend.split_data")
os.system("python -m data_expend.collect_tag")
os.system("python -m data_expend.collect_label")
os.system("python -m data_expend.write_metadata")

