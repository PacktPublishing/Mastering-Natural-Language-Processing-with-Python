import nltk
from nltk.util import ngrams
from nltk.corpus import alpino
print(alpino.words())
unigrams=ngrams(alpino.words(),1)
for i in unigrams:
    print(i)
