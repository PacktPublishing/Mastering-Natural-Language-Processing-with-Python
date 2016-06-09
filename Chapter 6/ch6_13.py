import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
wn.synsets('cat')
wn.synsets('cat', pos=wn.VERB)
wn.synset('cat.n.01')
print(wn.synset('cat.n.01').definition())
print(len(wn.synset('cat.n.01').examples()))
print(wn.synset('cat.n.01').lemmas())
print([str(lemma.name()) for lemma in wn.synset('cat.n.01').lemmas()])
print(wn.lemma('cat.n.01.cat').synset())

