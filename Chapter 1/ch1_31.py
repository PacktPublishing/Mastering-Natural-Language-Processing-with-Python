import nltk
from replacers import WordReplacer
replacer=WordReplacer({'congrats':'congratulations'})
print(replacer.replace('congrats'))
print(replacer.replace('maths'))
