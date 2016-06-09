import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
stemmer_output=PorterStemmer()
print(stemmer_output.stem('happiness'))
lemmatizer_output=WordNetLemmatizer()
print(lemmatizer_output.lemmatize('happiness'))


