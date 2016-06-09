import nltk
from nltk.tokenize import regexp_tokenize
sent="Don't hesitate to ask questions"
print(regexp_tokenize(sent, pattern='\w+|\$[\d\.]+|\S+'))


