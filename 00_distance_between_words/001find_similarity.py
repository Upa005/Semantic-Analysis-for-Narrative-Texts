# Python 3.6 program to find similarity of words from an input text file.
# INPUT -> any arbitrary input text file
# OUTPUT -> all the words whose similarity is greater than or equal to 50%
# Package used -> nltk wordent

import nltk
import nltk.data
from nltk.tokenize import word_tokenize



# opening the file
with open('match.txt','r') as file:
    data=file.read()

#removing punctuations
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
word = tokenizer.tokenize(data)

#removing stopwords
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
word = [w for w in word if w not in english_stops and len(w)>3 and not w.isdigit()]
word = list(set(word))
print(word)

print ()
#finding similarity
from nltk.corpus import wordnet
for i in range(len(word)):
    #print(word[i])
    if wordnet.synsets(word[i]):
        s1 = wordnet.synsets(word[i])[0]

        for j in range(len(word)):
            if(i!=j):
                if wordnet.synsets(word[j]):
                    s2 = wordnet.synsets(word[j])[0]
                    d = wordnet.wup_similarity(s1, s2)
                    if d != None: and d>=0.5:
                        print ("%.2f \t%s \t%s"%(d,s1.name(),s2.name()))

