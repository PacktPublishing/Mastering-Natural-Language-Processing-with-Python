import nltk
chunkparser = nltk.RegexpParser("")
print(nltk.chunk.accuracy(chunkparser, nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=('NP',))))
