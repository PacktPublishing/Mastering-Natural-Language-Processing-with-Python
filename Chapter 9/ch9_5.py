import nltk
expr_read = nltk.sem.DrtExpression.fromstring
expr5 = expr_read('([x,y],[ram(x),food(y),eats(x,y)])')
expr6 = expr_read('([u,z],[PRO(u),coffee(z),drinks(u,z)])')
expr7=expr5+expr6
print(expr7.simplify())
print(expr7.simplify().resolve_anaphora())
