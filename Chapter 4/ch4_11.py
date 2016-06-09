import nltk
from nltk.tag import DefaultTagger
tag = DefaultTagger('NN')
print(tag.tag(['Beautiful', 'morning']))

