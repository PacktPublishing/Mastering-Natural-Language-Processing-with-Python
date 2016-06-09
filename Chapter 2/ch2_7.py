import nltk
from nltk.collocations import *
import nltk
text="Hello how are you doing ? I hope you find the book interesting"
tokens=nltk.wordpunct_tokenize(text)
fourgrams=nltk.collocations.QuadgramCollocationFinder.from_words(tokens)
for fourgram, freq in fourgrams.ngram_fd.items():
    print(fourgram,freq)
