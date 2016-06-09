import nltk
from nltk.tokenize import RegexpTokenizer
sent=" She secured 90.56 % in class X . She is a meritorious student"
capt = RegexpTokenizer('[A-Z]\w+')
print(capt.tokenize(sent))
