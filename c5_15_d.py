import nltk
from nltk.corpus import brown
words = brown.tagged_words()
bgram = nltk.bigrams(words)
tags = [b[1] for (a, b) in bgram if a[1] == 'NN']
fd = nltk.FreqDist(tags)
sort = sorted(fd.iteritems(), key = lambda d:d[1], reverse = True)
print sort[:20]
