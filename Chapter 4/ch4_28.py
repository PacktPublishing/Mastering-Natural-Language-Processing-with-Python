import nltk
from nltk.tag import DefaultTagger
from nltk.tag import tnt
from nltk.corpus import treebank
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
tnt_tagger=tnt.TnT()
unknown=DefaultTagger('NN')
tagger_tnt=tnt.TnT(unk=unknown,Trained=True)
tnt_tagger.train(training)
print(tnt_tagger.evaluate(testing))
