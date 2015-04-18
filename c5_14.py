import nltk
from nltk.corpus import brown
btw = brown.tagged_words()
fd = nltk.FreqDist(t for (w,t) in btw)
tag = sorted(set(fd.keys()))
for tag in tag:
    print tag
