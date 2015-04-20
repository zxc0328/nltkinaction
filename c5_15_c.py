import nltk
from nltk.corpus import brown
words = brown.tagged_words()
fd = nltk.FreqDist(val for (word,val) in words)
sort = sorted(fd.iteritems(), key = lambda d:d[1], reverse = True)
print "Top 20 most freq pos tags in brown"
print sort[:20]
