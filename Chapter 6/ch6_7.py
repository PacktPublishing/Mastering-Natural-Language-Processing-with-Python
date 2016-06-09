import nltk
sentences1 = nltk.corpus.treebank.tagged_sents()[17]
print(nltk.ne_chunk(sentences1, binary=True))
sentences2 = nltk.corpus.treebank.tagged_sents()[7]
print(nltk.ne_chunk(sentences2, binary=True))
print(nltk.ne_chunk(sentences2))

