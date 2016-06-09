import nltk
from nltk.tokenize import WhitespaceTokenizer
sent=" She secured 90.56 % in class X \n. She is a meritorious student\n"
print(list(WhitespaceTokenizer().span_tokenize(sent)))
