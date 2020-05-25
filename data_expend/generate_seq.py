#!/usr/bin/env python

from tokenizer_tools.tagset.offset.corpus import Corpus
import json
import os
import random


class Data_Expend():

    def __init__(self, config_filepath):
        self.config_filepath = config_filepath
        self.config = self.get_config()

    def get_config(self):
        '''
            从配置文件中读取配置信息
        '''
        with open(self.config_filepath, 'rb') as f:
            self.config = json.load(f)
        return self.config

    def get_list(self):

        # read data
        corpus = Corpus.read_from_file(self.config['data_corpus'])

        corpus_stat = corpus.generate_statistics()

        # raw entity list
        result_raw = {}
        for k, v in corpus_stat.entity_types.items():
            d = ["".join(i[0]) for i in v.most_common()]
            result_raw[k] = d

        # expend entity list
        # read mapping
        with open(self.config['mapping'], 'r', encoding='UTF-8') as f:
            map_list = json.load(f)

        # read meta
        with open(self.config['meta'], 'r', encoding='UTF-8') as f:
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
                            if len(list1) > self.config['max_list_expend']:
                                list2 = random.sample(list1, self.config['max_list_expend'])  # 随机取不超过固定大小的list值
                                list3.extend(list2)
                            else:
                                list3.extend(list1)
                    result_new[k] = list3

        return result_raw, result_new

    # merge entity list
    @classmethod
    def hebing(cls, A, B):
        for k, v in B.items():
            if k in A:
                A[k] += v
        return A

    # set entity list
    @classmethod
    def quchong(cls, C):
        for k, v in C.items():
            v1 = list(set(v))
            C[k] = v1
        return C

    def get_expend_res(self):
        # read data
        corpus = Corpus.read_from_file(self.config['data_corpus'])

        result_raw, result_new = Data_Expend(self.config['configure']).get_list()  # generate list

        result_hb = Data_Expend.hebing(result_raw, result_new)  # merge
        res = Data_Expend.quchong(result_hb)  # set

        # generate sequence pattern
        doc_pattern = corpus.generate_pattern()
        doc_pattern.write_to_file(self.config['sequence_expend'])

        # expend doc
        doc_expend = doc_pattern.render(res)
        doc_expend.write_to_file(self.config['data_expend_result'])


if __name__ == "__main__":

    conf = Data_Expend('./data/configure.json')
    conf.get_expend_res()
    print("data expend done!")










