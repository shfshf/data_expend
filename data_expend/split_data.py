#!/usr/bin/env python

import pathlib
from tokenizer_tools.conllz.iterator_reader import conllx_iterator_reader
from tokenizer_tools.split_data import split_data
from tokenizer_tools.conllz.writer import write_conllx


path = pathlib.Path('./data/mapping.json')
if path.exists():
    dir = ['./data/expend/data_expend.conllx']
else:
    dir = ['./data/all_data.conllx']

data = list(conllx_iterator_reader(dir))
train, dev, test = split_data(data)

with open('./data/final/train.conllx', 'wt') as fd:
    write_conllx(train, fd)

with open('./data/final/dev.conllx', 'wt') as fd:
    write_conllx(dev, fd)

with open('./data/final/test.conllx', 'wt') as fd:
    write_conllx(test, fd)

