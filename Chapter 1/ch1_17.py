import nltk
sent=" She secured 90.56 % in class X \n. She is a meritorious student\n"
from nltk.tokenize import SpaceTokenizer
print(SpaceTokenizer().tokenize(sent))
