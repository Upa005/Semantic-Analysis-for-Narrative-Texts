# take verbs and noun and plot their occurrence according to the section
import matplotlib.pyplot as plt
import nltk
import easygui
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import matplotlib.cm as cm
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
lemma = WordNetLemmatizer()

stop_words = {"other's",'o','oh','aah','ah','once','\'','a','\'s','|','but','time','regularly','till','this','as','Since','In','got','But','lot','there','A','a','against','The', 'in', ',' ,'.',  '! ', 'to', 'because', 'couldn', 'should', 'was', 'who', 'doesn', 'itself', 'has', 'below', 'were', 'each', 'before', 'while', 'from', 'hasn', 'hers', 'off', 'when', 'ma', 'both', 'which', 'here', 'can', 'over', 'further', 'not', 'these', 'now', 'shan', 'ourselves', 'no', 'whom', 'of', 'under', 'then', 'few', 'had', 'so', 'do', 'the', 'does', 'didn', 'their', 'if', 'mightn', 'how', 've', 'hadn', 'once', 'into', 'been', 'more', 'those', 'y', 'am', 'weren', 'too', 're', 'an', 'after', 'with', 'our', 's', 'at', 'why', 'only', 'your', 'again', 'wouldn', 'a', 'all', 'm', 'very', 'by', 'herself', 'having', 'and', 'is', 'as', 'some', 'needn', 'be', 'or', 'yourself', 'ours', 'yours', 'being', 'any', 'll', 'o', 'for', 'above', 'up', 'yourselves', 'ain', 'haven', 'down', 'doing', 'did', 'won', 'that',  'between', 'same', 'she', 'such', 'but', 'most', 'own', 'don', 'than', 'during', 'themselves', 'nor', 'just', 'until', 'where', 'them', 'about', 'theirs', 'd', 'what', 'aren', 'shouldn',  'are', 't', 'i', 'my', 'on', 'there', 'wasn', 'will', 'mustn', 'myself', 'out', 'isn', 'have', 'its', 'through', 'other','a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'did', 'do', ' done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'hence', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'It',  'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once',  'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the',  'themselves', 'then', 'thence',  'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'thick', 'thin', 'third',  'though', 'three', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'very', 'via', 'was',  'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'the','with', 'within', 'without', 'would', 'yet', 'your', 'yours', 'yourself', 'yourselves'}


def lemmatize_data(data):  # to lemmatize data from file ; # why done - so that it takes monkeys and monkey as a same word

    for i in range(len(data)):
        data[i] = data[i].split()
        ts = nltk.pos_tag(data[i])
        for j in range(len(ts)):
            if ts[j][1] == 'VBZ' or ts[j][1] == 'VB' or ts[j][1] == 'VBD' or ts[j][1] == 'VBN' or ts[j][
                1] == 'VBP' or ts[j][1] == 'VBG':
                t = lemma.lemmatize(ts[j][0], pos='v')
                data[i][j] = t

            elif ts[j][1] == 'NNP' or ts[j][1] == 'NNS' or ts[j][1] == 'NNPS' or ts[j][1] == 'NN':
                t = lemma.lemmatize(ts[j][0], pos='n')
                data[i][j] = t
    data = [' '.join(w) for w in data]
    data = ' '.join(data)
    #print(data)
    return data


def find_key_word(data): #finding noun and verb from data
    key_word = []
    data = data.replace('.','').replace(',','').replace(';','').replace(':','')
    data = data.split()

    for i in range(len(data)):

        data[i] = data[i].split()
        tagged_sentences = nltk.pos_tag(data[i])
        #print(tagged_sentences)
        if tagged_sentences:
            ts = tagged_sentences
            j = 0
            while j < len(ts):

                if ts[j][1] == 'VBZ' or ts[j][1] == 'VB' or ts[j][1] == 'VBD' or ts[j][1] == 'VBN' or ts[j][
                    1] == 'VBP' or ts[j][1] == 'VBG':
                    t = lemma.lemmatize(ts[j][0],pos ='v')
                    key_word.append(t)

                elif ts[j][1] == 'NNP' or ts[j][1] == 'NNS' or ts[j][1] == 'NNPS' or ts[j][1] == 'NN':
                    t = lemma.lemmatize(ts[j][0], pos='n')
                    key_word.append(t)

                j += 1
    key_word = [w.lower() for w in key_word if w.lower() not in stop_words]
    key = []
    [key.append(x) for x in key_word if x not in key] #to remove repeated words
    return key


file = easygui.fileopenbox()
#file = '01the_monkey_and_the_wedge.txt'
with open(file, 'r') as f:
    data = f.read()

#data = data[:int(0.5*len(data.split()))]
#print('File loaded is: ',file)
print(data)
key_word = find_key_word(data)
#key_word = ['merchant', 'employ', 'carpenter', 'mason', 'build', 'temple', 'garden', 'start', 'work', 'morning', 'meal', 'return', 'resume', 'day', 'group', 'monkey', 'arrive', 'site', 'watch', 'worker', 'leave', 'log', 'half-done', 'place', 'wedge', 'close', 'come', 'result', 'destiny', 'wise', 'say', 'interfere', 'grief']

print(key_word)
print(len(key_word))
d = lemmatize_data(data.split())
my_data = d.split()
my_data = [w for w in my_data if w not in stop_words]
my_data = " ".join(my_data)

my_data = my_data.split('.')

#print("+" * 40)
print('Number of sentences: ', len(my_data))

no_sen = int(input('How many sentences in each section? '))

#for no_sen in range(5):
j = 0
my_sec = []
while (j + 2* no_sen < len(my_data)):
    my_sec.append(my_data[j:j + no_sen])
    j += no_sen

if j < len(my_data):
    my_sec.append(my_data[j:])

#for i in my_sec:
#    print(i)
#print('\nTotal sections: ', len(my_sec))
#matrix = [[0 for x in range(len(my_sec))] for y in range(len(key_word))]
#matrix = [[] for x in range(len(key_word))]
matrix = []
j = 0
for user_word in key_word:
    present = 0

    count = [0 for i in range(len(my_sec))]
    for i in range(len(my_sec)):
        present = 0
        word_found = 0
        for k in range(len(my_sec[i])):
            if user_word in my_sec[i][k]:
                word_found += 1
                for m in (key_word):
                    if m in my_sec[i][k]:
                        present += 1
                        #print(my_sec[i][k],'--',m)
        count[i] = 0.5 * present + 0.5 * word_found

        present = 0
    matrix.append(count)
    j += 1
    #print(count, user_word)


flat = [x for sublist in matrix for x in sublist]
f = list(set(flat))
f.sort(reverse=True)
#print('f: ',f,'len: ',len(f))
x = []
y = []
color = [ 'r^','b^','g^','k^','m^','y^',
            'k+','k.',
         'b+','g+','r+','m+','y+','k+',
         'bs','gs','rs','cs','ms','ys','ks',
         'b*','g*','r*','c*','m*','y*','k*',
         'bo', 'go', 'ro', 'co', 'mo', 'yo', 'ko',
         ]

x1 = [x for x in range(len(my_sec))]
sec_name = ['sec'+str(x+1) for x in range(len(my_sec))]
plt.xticks(x1,sec_name)

y1 = [x for x in range(len(key_word))]
sec_name = ['sec'+str(x+1) for x in range(len(my_sec))]
plt.yticks(y1,key_word)



for k in range(len(f)):

    x1 = []
    y1 = []
    for i in range(len(key_word)):
        for j in range(len(my_sec)):
            if matrix[i][j] == f[k]:
                x1.append(j)
                y1.append(i)

    if f[k] == 0:
        plt.plot(x1, y1, 'c+',label=f[k])
    else:
       plt.plot(x1,y1,color[k],label = f[k])


plt.legend().draggable()
disp_x = 'Sections: sentences in each section'+str(no_sen)
plt.xlabel(disp_x)
plt.ylabel('Keywords')
#plt.grid()
plt.show()

