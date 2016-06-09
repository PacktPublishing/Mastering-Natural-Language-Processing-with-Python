import nltk
from nltk.corpus import brown
from nltk.tag import UnigramTagger
tagger = UnigramTagger(brown.tagged_sents(categories='news')[:700])
sentence = ['John','and','Smith','went','to','NY','and','Germany']
for word, tag in tagger.tag(sentence):
    print(word,'->',tag)
