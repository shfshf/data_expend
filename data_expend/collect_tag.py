#!/usr/bin/env python

import pathlib
from tokenizer_tools.tagset.offset.corpus import Corpus


path = pathlib.Path('./data/mapping.json')
if path.exists():
    dir = './data/expend/data_expend.conllx'
else:
    dir = './data/all_data.conllx'
corpus = Corpus.read_from_file(dir)

with open("data/final/entity.txt", "wt") as fd:
    fd.write("\n".join({span.entity for doc in corpus for span in doc.span_set}))
