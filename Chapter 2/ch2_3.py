import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.corpus import webtext
from nltk.metrics import BigramAssocMeasures
tokens=[t.lower() for t in webtext.words('grail.txt')]
words=BigramCollocationFinder.from_words(tokens)
print(words.nbest(BigramAssocMeasures.likelihood_ratio, 10))
