import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser2 = nltk.parse.BottomUpLeftCornerChartParser(gram1)
chart2 = parser2.chart_parse(sent)
print((chart2.num_edges()))
print((len(list(chart2.parses(gram1.start())))))
