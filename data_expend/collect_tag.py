#!/usr/bin/env python

import pathlib
import json
from tokenizer_tools.tagset.offset.corpus import Corpus

# read mapping
with open("./data/mapping.json", 'r', encoding='UTF-8') as f:
    map_list = json.load(f)

# path = pathlib.Path('./data/mapping.json')
# if path.exists():
if map_list:
    dir = './data/expend/data_expend.conllx'
else:
    dir = './data/all_data.conllx'
corpus = Corpus.read_from_file(dir)

with open("data/final/entity.txt", "wt") as fd:
    fd.write("\n".join({span.entity for doc in corpus for span in doc.span_set}))
