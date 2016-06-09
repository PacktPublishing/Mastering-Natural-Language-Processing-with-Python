import nltk
from nltk.corpus import treebank_chunk
print(treebank_chunk.chunked_sents()[1])
treebank_chunk.chunked_sents()[1].draw()
