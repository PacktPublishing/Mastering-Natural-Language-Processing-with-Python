import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser4 = nltk.parse.TopDownChartParser(gram1)
chart4 = parser4.chart_parse(sent)
print((chart4.num_edges()))
print((len(list(chart4.parses(gram1.start())))))
