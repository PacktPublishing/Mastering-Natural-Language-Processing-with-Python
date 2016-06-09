import nltk
import nltk.corpus
print(str(nltk.corpus.treebank).replace('\\\\','/'))
print(nltk.corpus.treebank.fileids())
from nltk.corpus import treebank
print(treebank.words('wsj_0007.mrg'))
print(treebank.tagged_words('wsj_0007.mrg'))

