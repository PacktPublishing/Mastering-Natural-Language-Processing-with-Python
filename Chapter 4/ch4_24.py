import nltk
from nltk.tag import AffixTagger
from nltk.corpus import treebank
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
prefixtag = AffixTagger(training, affix_length=4)
print(prefixtag.evaluate(testing))
