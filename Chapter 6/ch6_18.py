import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')
from nltk.corpus import genesis
genesis_ic = wn.ic(genesis, False, 0.0)
lion = wn.synset('lion.n.01')
cat = wn.synset('cat.n.01')
print(lion.res_similarity(cat, brown_ic))
print(lion.res_similarity(cat, genesis_ic))
print(lion.jcn_similarity(cat, brown_ic))
print(lion.jcn_similarity(cat, genesis_ic))
print(lion.lin_similarity(cat, semcor_ic))


