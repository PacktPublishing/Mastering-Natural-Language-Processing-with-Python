import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
print(sorted(wn.langs()))
print(wn.synset('cat.n.01').lemma_names('ita'))
print(sorted(wn.synset('cat.n.01').lemmas('dan')))
print(sorted(wn.synset('cat.n.01').lemmas('por')))
print(len(wordnet.all_lemma_names(pos='n', lang='jpn')))
cat = wn.synset('cat.n.01')
print(cat.hypernyms())
print(cat.hyponyms())
print(cat.member_holonyms())
print(cat.root_hypernyms())
print(wn.synset('cat.n.01').lowest_common_hypernyms(wn.synset('dog.n.01')))
