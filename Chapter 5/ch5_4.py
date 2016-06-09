import nltk
from nltk.corpus import treebank_chunk
print(treebank_chunk.chunked_sents()[1].leaves())
print(treebank_chunk.chunked_sents()[1].pos())
print(treebank_chunk.chunked_sents()[1].productions())
print(nltk.corpus.treebank.tagged_words())
