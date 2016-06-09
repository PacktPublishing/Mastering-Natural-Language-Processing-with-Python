import nltk
from nltk.corpus import brown
sentences=brown.tagged_sents(categories='news')
sz=int(len(sentences)*0.8)
training_sents = sentences[:sz]
testing_sents=sentences[sz:]
bigram_tagger=nltk.UnigramTagger(training_sents)
bigram_tagger=nltk.BigramTagger(training_sents)
print(bigram_tagger.tag(sentences[2008]))
un_sent=sentences[4203]
print(bigram_tagger.tag(un_sent))
print(bigram_tagger.evaluate(testing_sents))
