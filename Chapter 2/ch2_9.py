import nltk
cor = nltk.corpus.brown.tagged_sents(categories='adventure')[:500]
print(len(cor))
from nltk.util import unique_list
tag_set = unique_list(tag for sent in cor for (word,tag) in sent)
print(len(tag_set))
symbols = unique_list(word for sent in cor for (word,tag) in sent)
print(len(symbols))
print(len(tag_set))
symbols = unique_list(word for sent in cor for (word,tag) in sent)
print(len(symbols))
trainer = nltk.tag.HiddenMarkovModelTrainer(tag_set, symbols)
train_corpus = []
test_corpus = []
for i in range(len(cor)):
    if i % 10:
        train_corpus+=[cor[i]]
    else:
        test_corpus+=[cor[i]]
print(len(train_corpus))
print(len(test_corpus))
 
    
