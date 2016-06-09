import nltk
from nltk.tag import BigramTagger
from nltk.corpus import treebank
training_1= treebank.tagged_sents()[:7000]
bigramtagger=BigramTagger(training_1)
print(treebank.sents()[0])
print(bigramtagger.tag(treebank.sents()[0]))
testing_1 = treebank.tagged_sents()[2000:]
print(bigramtagger.evaluate(testing_1))

