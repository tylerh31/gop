# encoding=utf8
import sys  
import nltk
from nltk.collocations import *

reload(sys)
sys.setdefaultencoding('utf8')

f=open('platform.txt','rU')
raw=f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

text.collocations()

stop_words = set(nltk.corpus.stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/', "n't", "'s", "'m", "_", "-", '—'])
results = [token.lower() for token in tokens if token.lower() not in stop_words]
fdist = nltk.FreqDist(results)

for word, frequency in fdist.most_common(50):
    print('%s: %d' % (word, frequency)).encode('utf-8')

bigrams = nltk.bigrams(results)
cfd = nltk.ConditionalFreqDist(bigrams)

# print list(cfd['god'])