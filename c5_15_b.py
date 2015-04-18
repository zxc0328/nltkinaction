import nltk
from nltk.corpus import brown
wl = brown.tagged_words()
data = nltk.ConditionalFreqDist((w.lower(),tag) for (w,tag) in wl)
li = {}
for word in sorted(data.conditions()):
    li.update({word, len(data[word])})

sort = sorted(li.iteritems(), key = lambda d:d[1], reverse = True)
sort[:20]

for word, val in sort:
	if len(data[word]) > 9:
		tags = data[word].keys()
		print word, ' '.join(tags)
