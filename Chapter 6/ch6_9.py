import nltk
sentence = "I went to Greece to meet John";
tok=nltk.word_tokenize(sentence)
pos_tag=nltk.pos_tag(tok)
print(nltk.ne_chunk(pos_tag))
