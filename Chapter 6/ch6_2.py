import nltk
input_expr = nltk.sem.Expression.fromstring
print(input_expr('X | (Y -> Z)'))
print(input_expr('-(X & Y)'))
print(input_expr('X & Y'))
print(input_expr('X <-> -- X'))
