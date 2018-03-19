#Program : 1) Display the most frequent words appearing in the program
#          2) User will input a keyword, the program will show the words related to that keyword (noun or verb)
import nltk
import easygui
file = easygui.fileopenbox()
with open(file,'r') as file:
    data = file.read()

stop_words = {'A','|','but','"', '\'','till','this','This','There','As','In','got','But','lot','there','A','a','against','The', 'in', ',' ,'.',  '! ', 'to', 'because', 'couldn', 'should', 'was', 'who', 'doesn', 'itself', 'has', 'below', 'were', 'each', 'before', 'while', 'from', 'hasn', 'hers', 'off', 'when', 'ma', 'both', 'which', 'his', 'here', 'can', 'over', 'further', 'not', 'these', 'now', 'shan', 'ourselves', 'no', 'whom', 'of', 'under', 'then', 'few', 'had', 'so', 'do', 'the', 'does', 'didn', 'their', 'if', 'mightn', 'how', 've', 'hadn', 'once', 'into', 'been', 'more', 'those', 'y', 'am', 'weren', 'too', 're', 'an', 'after', 'with', 'our', 's', 'at', 'why', 'only', 'your', 'again', 'wouldn', 'a', 'all', 'm', 'very', 'by', 'herself', 'having', 'and', 'is', 'as', 'some', 'needn', 'be', 'or', 'yourself', 'ours', 'yours', 'being', 'any', 'll', 'o', 'for', 'above', 'up', 'yourselves', 'ain', 'haven', 'down', 'doing', 'did', 'won', 'that', 'himself', 'between', 'same', 'she', 'such', 'this', 'but', 'most', 'own', 'don', 'than', 'during', 'themselves', 'nor', 'just', 'until', 'where', 'them', 'about', 'theirs', 'd', 'what', 'aren', 'shouldn', 'it', 'are', 't', 'i', 'my', 'on', 'there', 'wasn', 'will', 'mustn', 'myself', 'out', 'isn', 'have', 'its', 'through', 'other','a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'did', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'hence', 'here', 'hereafter', 'hereby', 'herein', 'hereupon',  'herself',  'himself', 'his', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the',  'themselves', 'then', 'thence',  'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'thick', 'thin', 'third',  'though', 'three', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'very', 'via', 'was',  'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'the','with', 'within', 'without', 'would', 'yet', 'your', 'yours', 'yourself', 'yourselves'}
#removed stopwords - filter_data
data = [w for w in data.split() if w not in stop_words]
#print(f_d)
data = ' '.join(data)
data = data.split('.') #filter_para


#d = f_p#.split('.') #filter_sentence
noun = ''
pr = ''
d= data
#replaced pronoun
for i in range(len(d)):
    d[i] = d[i].split()
    t_s = nltk.pos_tag(d[i])
    #print(t_s)
    for j in range(len(t_s)):
        if t_s[j][1] == 'PRP$' or t_s[j][1] == 'PRP':
            d[i] = [item.replace(t_s[j][0],noun) for item in d[i]]
           
    for j in range(len(t_s)):
        if t_s[j][1] == 'NNP' or t_s[j][1] == 'NNS':
            noun = t_s[j][0]
#print (d)

#finding frequency
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

dd = [' '.join(w) for w in d]
dd = ', '.join(dd)
dd = dd.replace(',','')
dd = dd.lower()
key = []
for i in range(len(data)):

    #removing stopwords
    #store[i] = [w for w in data[i].split() if w not in stop_words]

    #tagging the words
    sentence = data[i]
    word = " ".join(sentence)
    sentences = nltk.sent_tokenize(word)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    #print(tagged_sentences)

    
    #finding subject, verb and object
    if tagged_sentences:
        ts = tagged_sentences[0]
        j=0

        while j< len(ts):

            if ts[j][1] == 'NNP' or ts[j][1] == 'PRP' or ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN'or ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
                key.append(ts[j][0])
            j+=1

key = ' '.join(key)
key = key.lower()           
dictionary = wordListToFreqDict(key.split())
sort_dict = sortFreqDict(dictionary)

print()
print('The keywords are: ')
print()
l = 0
more = 'y'
while l<len(sort_dict) and (more == 'y' or more == 'Y'):
    #l = l+10
    for s in sort_dict[l:l+10]: print(str(s))
    print()
    more = input('Want to know more(y/n) ')
    l = l+10
    
store = []
print()
print('='*40)
print()
userkey = input('Enter your keywords: ')
userkey=userkey.lower()
data= [' '.join(w) for w in d]
if userkey in dd:
    #print('find')
    for i in range(len(data)):
        #print(data[i])
        if userkey in data[i].lower():
            store.append(data[i])
            store.append(data[i+1])
            if i>1:
                store.append(data[i-1])
else:
    print('Sorry! The word in not in the found')
    exit()
print('=' *40)
print('\nSentences related to your keyword: \n')
print(store)

rel_key = []
for i in range(len(store)):
    
    #tagging the words
    sentence = store[i]
    #word = " ".join(sentence)
    word = sentence
    sentences = nltk.sent_tokenize(word)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    #print(tagged_sentences)

    
    #finding subject, verb and object
    if tagged_sentences:
        ts = tagged_sentences[0]
        j=0

        while j< len(ts):

            if ts[j][1] == 'NNP' or ts[j][1] == 'PRP' or ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN'or ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
                rel_key.append(ts[j][0])
            j+=1


    
rk = ' '.join(rel_key)
rk = rk.lower()
dictionary = wordListToFreqDict(rk.split())
sort_dict = sortFreqDict(dictionary)


print('\nRelated keywords: ')
print()
l = 0
more = 'y'
while l<len(sort_dict) and (more == 'y' or more == 'Y'):
    #l = l+10
    for s in sort_dict[l:l+10]: print(str(s))
    print()
    more = input('Want to know more(y/n) ')
    l = l+10
 



