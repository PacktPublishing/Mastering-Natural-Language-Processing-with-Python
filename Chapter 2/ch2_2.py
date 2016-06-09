import nltk
from nltk.util import ngrams
from nltk.corpus import alpino
print(alpino.words())
quadgrams=ngrams(alpino.words(),4)
for i in quadgrams:
    print(i)
