import nltk
from nltk.collocations import *
text1="Hardwork is the key to success. Never give up!"
word = nltk.wordpunct_tokenize(text1)
finder = BigramCollocationFinder.from_words(word)
bigram_measures = nltk.collocations.BigramAssocMeasures()
value = finder.score_ngrams(bigram_measures.raw_freq)
print(sorted(bigram for bigram, score in value))
