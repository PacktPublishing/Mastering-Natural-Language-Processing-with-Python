import nltk
import os,os.path
create = os.path.expanduser('~/nltkdoc')
if not os.path.exists(create):
    os.mkdir(create)
print(os.path.exists(create))
import nltk.data
print(create in nltk.data.path)

