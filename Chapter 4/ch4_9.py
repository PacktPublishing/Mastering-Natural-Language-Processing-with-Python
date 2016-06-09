import nltk
from nltk.corpus import treebank	
treebank_tagged = treebank.tagged_words(tagset='universal')
tagpairs = nltk.bigrams(treebank_tagged)
preceders_noun = [x[1] for (x, y) in tagpairs if y[1] == 'NOUN']
freqdist = nltk.FreqDist(preceders_noun)
print([tag for (tag, _) in freqdist.most_common()])
