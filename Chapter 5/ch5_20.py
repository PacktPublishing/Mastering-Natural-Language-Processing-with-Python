import nltk
from nltk.corpus import treebank
from itertools import islice
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
tokens = "Jack told Bob to bring my cookie".split()
grammar = toy_pcfg2
print(grammar)
