import nltk
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
text=" Hello everyone. Hope all are fine and doing well. Hope you find the book interesting"
print(tokenizer.tokenize(text))
