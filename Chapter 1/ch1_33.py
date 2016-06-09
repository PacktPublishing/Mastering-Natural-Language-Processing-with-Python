from __future__ import print_function
from nltk.metrics import *
training='PERSON OTHER PERSON OTHER OTHER ORGANIZATION'.split()
testing='PERSON OTHER OTHER OTHER OTHER OTHER'.split()
print(accuracy(training,testing))
trainset=set(training)
testset=set(testing)
precision(trainset,testset)
print(recall(trainset,testset))
print(f_measure(trainset,testset))
 
