import nltk
from nltk.corpus import brown
sentences=brown.tagged_sents(categories='news')
sz=int(len(sentences)*0.8)
print(sz)
training_sents = sentences[:sz]
print(testing_sents=sentences[sz:])
unigram_tagger=nltk.UnigramTagger(training_sents)
print(unigram_tagger.evaluate(testing_sents))

