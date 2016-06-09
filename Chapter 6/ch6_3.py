import nltk
value = nltk.Valuation([('X', True), ('Y', False), ('Z', True)])
print(value['Z'])
domain = set()
v = nltk.Assignment(domain)
u = nltk.Model(domain, value)
print(u.evaluate('(X & Y)', v))
print(u.evaluate('-(X & Y)', v))
print(u.evaluate('(X & Z)', v))
print(u.evaluate('(X | Y)', v))

