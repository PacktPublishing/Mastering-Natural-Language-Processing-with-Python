import nltk
from nltk.tokenize import word_tokenize
from replacers import RegexpReplacer
replacer=RegexpReplacer()
word_tokenize("Don't hesitate to ask questions")
print(word_tokenize(replacer.replace("Don't hesitate to ask questions")))
