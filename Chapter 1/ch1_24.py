import nltk
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
words=["Don't", 'hesitate','to','ask','questions']
print([word for word in words if word not in stops])
