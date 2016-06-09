import nltk
import random
from nltk.corpus import movie_reviews
docs = [(list(movie_reviews.words(fid)), cat) for cat in movie_reviews.categories() for fid in movie_reviews.fileids(cat)]
random.shuffle(docs)
all_tokens = nltk.FreqDist(x.lower() for x in movie_reviews.words())
token_features = list(all_tokens.keys())[:2000]
print(token_features[:100])
 
def doc_features(docs):
    doc_words = set(docs)
    features = {}
    for word in token_features:
        features['contains(%s)' % word] = (word in doc_words)
        return features

print(doc_features(movie_reviews.words('pos/cv957_8737.txt')))
feature_sets = [(doc_features(d), c) for (d,c) in docs]
train_sets, test_sets = feature_sets[100:], feature_sets[:100]
classifiers = nltk.NaiveBayesClassifier.train(train_sets)
print(nltk.classify.accuracy(classifiers, test_sets))
classifiers.show_most_informative_features(5)
