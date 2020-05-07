#!/usr/bin/env python

from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("./data/expend/data_expend.conllx")

with open("data/final/entity.txt", "wt") as fd:
    fd.write("\n".join({span.entity for doc in corpus for span in doc.span_set}))
