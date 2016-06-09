import nltk
noun1=[("financial","NN"),("year","NN"),("account","NN"),("summary","NN")]
gram="NP:{<NN>+}"
find = nltk.RegexpParser(gram)
print(find.parse(noun1))
x=find.parse(noun1)
x.draw()
