import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser9 = nltk.parse.EarleyChartParser(gram1)
chart9 = parser9.chart_parse(sent)
print((chart9.num_edges()))
print((len(list(chart9.parses(gram1.start())))))
