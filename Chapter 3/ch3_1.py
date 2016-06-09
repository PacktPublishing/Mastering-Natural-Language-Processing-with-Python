import nltk
from nltk.stem import PorterStemmer
stemmerporter = PorterStemmer()
print(stemmerporter.stem('working'))
print(stemmerporter.stem('happiness'))

