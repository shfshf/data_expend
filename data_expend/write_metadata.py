#!/usr/bin/env python

import datetime
import json
import pathlib

from tokenizer_tools.conllz.iterator_reader import conllx_iterator_reader

# read mapping
with open("./data/mapping.json", 'r', encoding='UTF-8') as f:
    map_list = json.load(f)

# path = pathlib.Path('./data/mapping.json')
# if path.exists():
if map_list:
    dir = ['./data/expend/data_expend.conllx']
else:
    dir = ['./data/all_data.conllx']
data = list(conllx_iterator_reader(dir))
train_data = list(conllx_iterator_reader(["data/final/train.conllx"]))
dev_data = list(conllx_iterator_reader(["data/final/dev.conllx"]))
test_data = list(conllx_iterator_reader(["data/final/test.conllx"]))

metdata = {
    "data": {
        "whole_data_size": len(data),
        "train_data_size": len(train_data),
        "dev_data_size": len(dev_data),
        "test_data_size": len(test_data),
    },
    "create_time": datetime.datetime.now().isoformat(),
}

with open("data/final/metadata.json", "wt") as fd:
    json.dump(metdata, fd)

print("data process finished ! ")
