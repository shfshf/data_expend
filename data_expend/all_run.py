import os

# os.system("python -m data_expend.dict_to_json")
os.system("python -m data_expend.json_to_conllx")
os.system("python -m data_expend.generate_seq")
# os.system("python -m data_expend.merge_data")
os.system("python -m data_expend.split_data")
os.system("python -m data_expend.collect_tag")
# os.system("python -m data_expend.collect_label")
os.system("python -m data_expend.write_metadata")
