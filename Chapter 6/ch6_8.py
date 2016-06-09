import nltk
from nltk.corpus import conll2002
for documents in conll2002.chunked_sents('ned.train')[25]:
    print(documents)
