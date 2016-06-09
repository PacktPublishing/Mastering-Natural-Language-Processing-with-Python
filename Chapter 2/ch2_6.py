import nltk
from nltk.util import ngrams
from nltk.corpus import alpino
print(alpino.words())
bigrams_tokens=ngrams(alpino.words(),2)
for i in bigrams_tokens:
    print(i) 
