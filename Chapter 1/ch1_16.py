import nltk
from nltk.tokenize import BlanklineTokenizer
sent=" She secured 90.56 % in class X \n. She is a meritorious student\n"
print(BlanklineTokenizer().tokenize(sent))
from nltk.tokenize import LineTokenizer
print(LineTokenizer(blanklines='keep').tokenize(sent))
print(LineTokenizer(blanklines='discard').tokenize(sent))
