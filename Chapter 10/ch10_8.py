import nltk
from nltk.corpus import brown
sentences = brown.tagged_sents(categories='news')
sent = brown.sents(categories='news')
pattern = [(r'(January)$','Jan')]
regexpr_tagger = nltk.RegexpTagger(pattern)
print(regexpr_tagger.tag(sent[3]))
print(regexpr_tagger.evaluate(sentences))

