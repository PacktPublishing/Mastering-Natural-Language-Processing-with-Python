import nltk
from nltk.util import ngrams
sent=" Hello , please read the book thoroughly . If you have any queries , then don't hesitate to ask . There is no shortcut to success ."
n=5
fivegrams=ngrams(sent.split(),n)
for grams in fivegrams:
    print(grams)
