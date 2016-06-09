import nltk
from nltk.tag import BigramTagger, TrigramTagger
from nltk.corpus import treebank
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
bigramtag = BigramTagger(training)
print(bigramtag.evaluate(testing))
trigramtag = TrigramTagger(training)
print(trigramtag.evaluate(testing))
