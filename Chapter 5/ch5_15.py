import nltk
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent=sent[25]
sent=testingsent[0]
parser6 = nltk.parse.IncrementalBottomUpLeftCornerChartParser(gram1)
chart6 = parser6.chart_parse(sent)
print((chart6.num_edges()))
print((len(list(chart6.parses(gram1.start())))))

