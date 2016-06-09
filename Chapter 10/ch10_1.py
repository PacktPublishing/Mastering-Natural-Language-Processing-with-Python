import nltk
from nltk.corpus import brown
sentences=brown.tagged_sents(categories='news')
sent=brown.sents(categories='news')
unigram_sent=nltk.UnigramTagger(sentences)
print(unigram_sent.tag(sent[2008]))
print(unigram_sent.evaluate(sentences))
