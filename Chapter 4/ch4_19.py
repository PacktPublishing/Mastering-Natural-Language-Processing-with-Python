import nltk
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger
from nltk.corpus import treebank
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
tag1=DefaultTagger('NN')
tag2=UnigramTagger(training,backoff=tag1)
print(tag2.evaluate(testing))
