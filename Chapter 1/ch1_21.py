text=[" It is a pleasant evening.","Guests, who came from US arrived at the venue","Food was tasty."]
from nltk.tokenize import word_tokenize
tokenized_docs=[word_tokenize(doc) for doc in text]
print(tokenized_docs)
