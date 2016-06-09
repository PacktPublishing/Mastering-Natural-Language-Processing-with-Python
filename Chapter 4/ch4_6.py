import nltk
sentence='''The/DT sacred/VBN Ganga/NNP flows/VBZ in/IN this/DT region/NN ./. This/DT is/VBZ a/DT pilgrimage/NN ./. People/NNP from/IN all/DT over/IN the/DT country/NN visit/NN this/DT place/NN ./. '''
print([nltk.tag.str2tuple(t) for t in sentence.split()])
