import nltk
from nltk.tag import tnt
from nltk.corpus import treebank
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
tnt_tagger=tnt.TnT()
tnt_tagger.train(training)
print(tnt_tagger.evaluate(testing))
