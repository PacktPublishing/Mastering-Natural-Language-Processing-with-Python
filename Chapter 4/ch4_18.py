import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger
unitag = UnigramTagger(model={'Vinken': 'NN'})
print(unitag.tag(treebank.sents()[0]))
