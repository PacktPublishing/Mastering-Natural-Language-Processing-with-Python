import nltk
from nltk.tokenize.util import string_span_tokenize
sent=" She secured 90.56 % in class X \n. She is a meritorious student\n"
print(list(string_span_tokenize(sent, " ")))
