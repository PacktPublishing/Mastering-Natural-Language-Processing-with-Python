import nltk
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
print(len(sent))
testingsent=sent[25]
print(testingsent[1])
print(testingsent[0])
sent=testingsent[0]
