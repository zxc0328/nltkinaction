import nltk
from nltk.corpus import brown
from __future__ import division
btw = brown.tagged_words()
data = nltk.ConditionalFreqDist((word.lower(),tag) for (word, tag) in btw)
list = [(word, data[word].keys()) for word in data.conditions() if len(data[word]) == 1]
print len(list)/len(btw)
