import nltk
expr_read = nltk.sem.DrtExpression.fromstring
expr4 = expr_read('([],[(([x],[student(x)])->([y],[book(y),read(x,y)]))])')
print(expr4.fol())
