import nltk
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize.util import spans_to_relative
sent=" She secured 90.56 % in class X \n. She is a meritorious student\n"
print(list(spans_to_relative(WhitespaceTokenizer().span_tokenize(sent))))
