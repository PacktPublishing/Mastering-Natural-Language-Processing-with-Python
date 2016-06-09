import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer_output=WordNetLemmatizer()
print(lemmatizer_output.lemmatize('working'))
print(lemmatizer_output.lemmatize('working',pos='v'))
print(lemmatizer_output.lemmatize('works'))

