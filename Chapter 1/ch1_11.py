import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer('\s+',gaps=True)
print(tokenizer.tokenize("Don't hesitate to ask questions"))
