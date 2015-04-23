import nltk
from nltk.corpus import brown
def process(sentence):
	for (w1,t1), (w2,t2), (w3, t3) in nltk.trigrams(sentence):
		if (t1== 'IN' and t2 == 'AT' and t3.startswith('NN')):
			print w1, w2, w3

bts = brown.tagged_sents()
for s in bts:
	process(s)
