import nltk
from nltk.stem import LancasterStemmer
stemmerlan=LancasterStemmer()
print(stemmerlan.stem('working'))
print(stemmerlan.stem('happiness'))
