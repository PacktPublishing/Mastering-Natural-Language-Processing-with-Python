import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w']+")
print(tokenizer.tokenize("Don't hesitate to ask questions"))
