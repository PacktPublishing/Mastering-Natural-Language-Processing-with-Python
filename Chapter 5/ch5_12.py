import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser3 = nltk.parse.LeftCornerChartParser(gram1)
chart3 = parser3.chart_parse(sent)
print((chart3.num_edges()))
print((len(list(chart3.parses(gram1.start())))))
