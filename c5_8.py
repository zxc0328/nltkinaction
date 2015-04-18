import nltk
from nltk.corpus import brown
btw_t = brown.tagged_words(categories='news')
tags_1 = [a[1] for (a,b) in nltk.bigrams(btw_t) if b[0] == 'went']
fd = nltk.FreqDist(tags_1)
tags_2 = [a[1] for (a,b) in nltk.bigrams(btw_t) if b[0] == 'go']
print "The freq table of pos tags of words in front of 'went':"
fd.tabulate()
print "The freq table of pos tags of words in front of 'go':"
fd = nltk.FreqDist(tags_2)
fd.tabulate()

