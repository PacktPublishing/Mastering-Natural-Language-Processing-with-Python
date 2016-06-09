import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser7 = nltk.parse.IncrementalLeftCornerChartParser(gram1)
chart7 = parser7.chart_parse(sent)
print((chart7.num_edges()))
print((len(list(chart7.parses(gram1.start())))))
