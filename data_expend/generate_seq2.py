#!/usr/bin/env python

from tokenizer_tools.tagset.offset.corpus import Corpus
import json
import os
import random


def get_list():

    # read data
    corpus = Corpus.read_from_file("./data/all_data.conllx")

    corpus_stat = corpus.generate_statistics()

    # raw entity list
    result_raw = {}
    for k, v in corpus_stat.entity_types.items():
        d = ["".join(i[0]) for i in v.most_common()]
        result_raw[k] = d

    # expend entity list
    # read mapping
    with open("./data/mapping.json", 'r', encoding='UTF-8') as f:
        map_list = json.load(f)

    # read meta
    with open("./data/dict/meta.json", 'r', encoding='UTF-8') as f:
        meta_list = json.load(f)

    # new entity list
    result_new = {}
    path = os.path.dirname(__file__)  # 获取当前目录
    for k, v in map_list.items():
        for m, n in meta_list.items():
            if v == m:
                list3 = []  # key 合并后的list集
                for i in n:
                    with open(path + '/data/dict/' + i) as f:
                        list1 = json.load(f)
                        if len(list1) > 100:
                            list2 = random.sample(list1, 100)  # 随机取不超过固定大小的list值
                            list3.extend(list2)
                        else:
                            list3.extend(list1)
                result_new[k] = list3

    return result_raw, result_new


# merge entity list
def hebing(A, B):
    for k, v in B.items():
        if k in A:
            A[k] += v
    return A


# set entity list
def quchong(C):
    for k, v in C.items():
        v1 = list(set(v))
        C[k] = v1
    return C


# read data

corpus = Corpus.read_from_file("./data/all_data.conllx")
result_raw, result_new = get_list()  # generate list

result_hb = hebing(result_raw, result_new)  # merge
res = quchong(result_hb)  # set

# generate sequence pattern
doc_pattern = corpus.generate_pattern()
doc_pattern.write_to_file("./data/sequence/seq.txt")

# expend doc
doc_expend = doc_pattern.render(res)
doc_expend.write_to_file("./data/expend/data_expend.conllx")

print("data expend done!")










