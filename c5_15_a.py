import nltk
from nltk.corpus import brown
word_list = brown.words()
fd = nltk.FreqDist(w for w in word_list)
for w,v in fd.items():
	if fd[w+"s"] > fd[w]:
		print w


        
