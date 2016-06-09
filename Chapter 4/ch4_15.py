import nltk
from nltk.corpus import words
print(words.fileids())
print(len(words.words('en')))
print(len(words.words('en-basic')))

