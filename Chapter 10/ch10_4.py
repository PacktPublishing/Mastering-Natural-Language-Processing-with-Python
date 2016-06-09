import nltk
from nltk.corpus import brown
sentences=brown.tagged_sents(categories='news')
sz=int(len(sentences)*0.8)
training_sents = sentences[:sz]
testing_sents=sentences[sz:]
s0=nltk.DefaultTagger('NNP')
s1=nltk.UnigramTagger(training_sents,backoff=s0)
s2=nltk.BigramTagger(training_sents,backoff=s1)
print(s2.evaluate(testing_sents))

