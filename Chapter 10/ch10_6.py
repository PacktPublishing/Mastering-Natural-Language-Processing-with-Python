import nltk
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)
print(nltk.chunk.accuracy(cp, nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=('NP',))))
