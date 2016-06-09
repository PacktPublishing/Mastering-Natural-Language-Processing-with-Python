import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser8 = nltk.parse.IncrementalTopDownChartParser(gram1)
chart8 = parser8.chart_parse(sent)
print((chart8.num_edges()))
print((len(list(chart8.parses(gram1.start())))))
