#!/usr/bin/env python

from tokenizer_tools.tagset.offset.corpus import Corpus
import json
import os


# read data
corpus = Corpus.read_from_file("./data/domain/data.conllx")

corpus_stat = corpus.generate_statistics()

# raw entity list
result_raw = {}
for k, v in corpus_stat.entity_types.items():
    d = ["".join(i[0]) for i in v.most_common()]
    result_raw[k] = d

# expend entity list
with open("./data/mapping.json", 'r', encoding='UTF-8') as f:
    map_list = json.load(f)

# new entity list
result_new = {}
path = os.path.dirname(__file__)  # 获取当前目录
for k, v in map_list.items():
    with open(path + '/data/' + v + '.json') as f:
        list1 = json.load(f)
    result_new[k] = list1


# merge entity list
def hebing(A, B):
    for k, v in B.items():
        A[k] = A.get(k, 0) + v
    return A


result_hb = hebing(result_raw, result_new)


# set entity list
def quchong(C):
    for k, v in C.items():
        v1 = list(set(v))
        C[k] = v1
    return C


res = quchong(result_hb)

# generate sequence pattern
doc_pattern = corpus.generate_pattern()
doc_pattern.write_to_file("./data/sequence/seq.txt")

# expend doc
doc_expend = doc_pattern.render(res)
doc_expend.write_to_file("./data/expend/data_expend.conllx")