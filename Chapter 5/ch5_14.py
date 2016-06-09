import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser5 = nltk.parse.IncrementalBottomUpChartParser(gram1)
chart5 = parser5.chart_parse(sent)
print((chart5.num_edges()))
print((len(list(chart5.parses(gram1.start())))))

