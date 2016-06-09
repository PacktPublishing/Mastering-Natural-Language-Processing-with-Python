import nltk
from nltk.tag import UnigramTagger
from nltk.corpus import treebank
training= treebank.tagged_sents()[:7000]
unitagger=UnigramTagger(training)
print(treebank.sents()[0])
print(unitagger.tag(treebank.sents()[0]))
