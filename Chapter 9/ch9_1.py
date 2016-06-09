import nltk
expr_read = nltk.sem.DrtExpression.fromstring
expr1 = expr_read('([x], [John(x), Went(x)])')
print(expr1)
expr1.draw()
print(expr1.fol())
