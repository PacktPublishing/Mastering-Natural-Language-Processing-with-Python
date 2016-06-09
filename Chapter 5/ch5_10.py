import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser1 = nltk.parse.BottomUpChartParser(gram1)
chart1 = parser1.chart_parse(sent)
print((chart1.num_edges()))
print((len(list(chart1.parses(gram1.start())))))

