#!/usr/bin/env python

import os
import pathlib

from tokenizer_tools.conllz.writer import write_conllx
from tokenizer_tools.tagset.offset.corpus import Corpus

from data_expend.processor import process_one_line, CheckFailedError


def make_dir():
    dirs = ['./data/domain', './data/error', './data/sequence', './data/final', './data/expend']
    for i in dirs:
        if not os.path.exists(i):
            os.makedirs(i)


def to_conllx(file_prefix):
    base_name, _ = os.path.splitext(file_prefix)

    log_file = './data/error/{}.error'.format(base_name)

    with open('./data/raw/{}'.format(file_prefix)) as fd, open(log_file, 'wt') as logger:
        output_lines = []
        seq_list = []
        for raw_line in fd:
            line = raw_line.strip()
            if not line:
                continue
            try:
                seq, sentence = process_one_line(line, logger)
            except CheckFailedError as e:
                continue
            else:
                seq_list.append(seq)
                output_lines.append(sentence)

        # write_conll(output_lines, 'data/{}.text'.format(file_prefix))
        output_file = './data/domain/{}.conllx'.format(base_name)
        # with open('./data/domain/{}.conllx'.format(base_name), 'wt') as output_fd:
            # write_conllx(output_lines, output_fd)
        Corpus(seq_list).write_to_file(output_file)


if __name__ == "__main__":

    make_dir()

    input_file_list = [i.name for i in pathlib.Path('./data/raw').iterdir() if i.is_file()]

    for input_file in input_file_list:
        to_conllx(input_file)






