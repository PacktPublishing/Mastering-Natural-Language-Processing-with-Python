import nltk
from nltk.corpus import stopwords
print(stopwords.words('english'))
def para_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    para = [w for w in text if w.lower() not in stopwords]
    return len(para) / len(text)
print(para_fraction(nltk.corpus.reuters.words()))
print(para_fraction(nltk.corpus.inaugural.words()))

