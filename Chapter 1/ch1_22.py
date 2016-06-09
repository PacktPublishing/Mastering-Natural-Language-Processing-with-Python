import re
import string
text=[" It is a pleasant evening.","Guests, who came from US arrived at the venue","Food was tasty."]
from nltk.tokenize import word_tokenize
tokenized_docs=[word_tokenize(doc) for doc in text]
x=re.compile('[%s]' % re.escape(string.punctuation))
tokenized_docs_no_punctuation = []
for review in tokenized_docs:
    new_review = []
    for token in review: 
        new_token = x.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    tokenized_docs_no_punctuation.append(new_review)	
print(tokenized_docs_no_punctuation)
