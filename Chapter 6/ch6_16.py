import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
lion = wn.synset('lion.n.01')
cat = wn.synset('cat.n.01')
print(lion.lch_similarity(cat))
