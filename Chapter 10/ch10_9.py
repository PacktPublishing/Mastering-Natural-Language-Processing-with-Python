import nltk
from nltk.corpus import brown
freqd = nltk.FreqDist(brown.words(categories='news'))
cfreqd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
mostfreq_words = freqd.most_common(100)
likelytags = dict((word, cfreqd[word].max()) for (word, _) in mostfreq_words)
baselinetagger = nltk.UnigramTagger(model=likelytags)

sent = brown.sents(categories='news')[3]
print(baselinetagger.tag(sent))
