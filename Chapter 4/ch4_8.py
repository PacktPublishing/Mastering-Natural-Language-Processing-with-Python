import nltk
from nltk.corpus import treebank
treebank_tagged = treebank.tagged_words(tagset='universal')
tag = nltk.FreqDist(tag for (word, tag) in treebank_tagged)
print(tag.most_common())
