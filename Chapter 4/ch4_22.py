import nltk
from nltk.corpus import treebank
from nltk import NgramTagger
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
quadgramtag = NgramTagger(4, training)
print(quadgramtag.evaluate(testing))

