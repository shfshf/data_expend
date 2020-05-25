#!/usr/bin/env python

import pathlib
from tokenizer_tools.tagset.offset.corpus import Corpus

path = pathlib.Path('./data/mapping.json')
if path.exists():
    dir = './data/expend/data_expend.conllx'
else:
    dir = './data/all_data.conllx'
corpus = Corpus.read_from_file(dir)

with open("data/final/label.txt", "wt") as fd:
    list1 = [doc.label for doc in corpus]
    fd.write("\n".join(set(list1)))

