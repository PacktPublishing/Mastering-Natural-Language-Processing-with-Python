import nltk
from nltk.stem import RegexpStemmer
stemmerregexp=RegexpStemmer('ing')
print(stemmerregexp.stem('working'))
print(stemmerregexp.stem('happiness'))
print(stemmerregexp.stem('pairing'))

