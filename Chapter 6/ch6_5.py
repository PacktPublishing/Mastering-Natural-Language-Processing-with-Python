import nltk
locations=[('Jaipur', 'IN', 'Rajasthan'),('Ajmer', 'IN', 'Rajasthan'),('Udaipur', 'IN', 'Rajasthan'),('Mumbai', 'IN', 'Maharashtra'),('Ahmedabad', 'IN', 'Gujrat')]
q = [x1 for (x1, relation, x2) in locations if x2=='Rajasthan']
print(q)
