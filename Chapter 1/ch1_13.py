import nltk
sent=" She secured 90.56 % in class X . She is a meritorious student"
from nltk.tokenize import BlanklineTokenizer
print(BlanklineTokenizer().tokenize(sent))
