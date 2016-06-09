import nltk
sent=[("A","DT"),("wise", "JJ"), ("small", "JJ"),("girl", "NN"), ("of", "IN"), ("village", "N"),  ("became", "VBD"), ("leader", "NN")]
sent=[("A","DT"),("wise", "JJ"), ("small", "JJ"),("girl", "NN"), ("of", "IN"), ("village", "NN"),  ("became", "VBD"), ("leader", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN><IN>?<NN>*}"
find = nltk.RegexpParser(grammar)
res = find.parse(sent)
print(res)
res.draw()
