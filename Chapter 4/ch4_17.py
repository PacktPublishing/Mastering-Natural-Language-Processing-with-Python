import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger
training= treebank.tagged_sents()[:7000]
unitagger=UnigramTagger(training)
testing = treebank.tagged_sents()[2000:]
print(unitagger.evaluate(testing))
