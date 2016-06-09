import nltk
from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)
spanishstemmer=SnowballStemmer('spanish')
print(spanishstemmer.stem('comiendo'))
frenchstemmer=SnowballStemmer('french')
print(frenchstemmer.stem('manger'))

