import nltk
french_tokenizer=nltk.data.load('tokenizers/punkt/french.pickle')
print(french_tokenizer.tokenize('Deux agressions en quelques jours, voilà ce qui a motivé hier matin le débrayage  collège franco-britanniquedeLevallois-Perret. Deux agressions en quelques jours, voilà ce qui a motivé hier matin le débrayage  Levallois. L’équipe pédagogique de ce collège de 750 élèves avait déjà été choquée par l’agression, janvier , d’un professeur d’histoire. L’équipe pédagogique de ce collège de 750 élèves avait déjà été choquée par l’agression, mercredi , d’un professeur d’histoire'))
