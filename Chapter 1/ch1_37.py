import nltk
from nltk.util import ngrams
from nltk.corpus import alpino
print(alpino.words())
trigrams_tokens=ngrams(alpino.words(),3)
for i in trigrams_tokens:
    print(i)
