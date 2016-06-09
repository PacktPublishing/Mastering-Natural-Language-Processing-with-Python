import nltk
from nltk.corpus import treebank
from itertools import islice
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
gram2 = PCFG.fromstring("""
	A -> B B [.3] | C B C [.7]
	B -> B D [.5] | C [.5]
	C -> 'a' [.1] | 'b' [0.9]
	D -> 'b' [1.0]
	""")
prod1 = gram2.productions()[0]
print(prod1)
prod2 = gram2.productions()[1]
print(prod2)
print(prod2.lhs())
print(prod2.rhs())
print((prod2.prob()))
print(gram2.start())
print(gram2.productions())
