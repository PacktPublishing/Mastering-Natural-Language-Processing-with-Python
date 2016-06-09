import nltk
from nltk.tag import AffixTagger
from nltk.corpus import treebank
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
prefixtagger=AffixTagger(training,affix_length=4)
prefixtagger3=AffixTagger(training,affix_length=3,backoff=prefixtagger)
print(prefixtagger3.evaluate(testing))
suffixtagger3=AffixTagger(training,affix_length=-3,backoff=prefixtagger3)
print(suffixtagger3.evaluate(testing))
suffixtagger4=AffixTagger(training,affix_length=-4,backoff=suffixtagger3)
print(suffixtagger4.evaluate(testing))

