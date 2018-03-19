import nltk
import easygui
from nltk.corpus import wordnet
from tkinter import *

stop_words = {'A','|','but','"', '\'','till','this','This','There','As','In','got','But','lot','there','A','a','against','The', 'in', ',' ,'.',  '! ', 'to', 'because', 'couldn', 'should', 'was', 'who', 'doesn', 'itself', 'has', 'below', 'were', 'each', 'before', 'while', 'from', 'hasn', 'hers', 'off', 'when', 'ma', 'both', 'which', 'his', 'here', 'can', 'over', 'further', 'not', 'these', 'now', 'shan', 'ourselves', 'no', 'whom', 'of', 'under', 'then', 'few', 'had', 'so', 'do', 'the', 'does', 'didn', 'their', 'if', 'mightn', 'how', 've', 'hadn', 'once', 'into', 'been', 'more', 'those', 'y', 'am', 'weren', 'too', 're', 'an', 'after', 'with', 'our', 's', 'at', 'why', 'only', 'your', 'again', 'wouldn', 'a', 'all', 'm', 'very', 'by', 'herself', 'having', 'and', 'is', 'as', 'some', 'needn', 'be', 'or', 'yourself', 'ours', 'yours', 'being', 'any', 'll', 'o', 'for', 'above', 'up', 'yourselves', 'ain', 'haven', 'down', 'doing', 'did', 'won', 'that', 'himself', 'between', 'same', 'she', 'such', 'this', 'but', 'most', 'own', 'don', 'than', 'during', 'themselves', 'nor', 'just', 'until', 'where', 'them', 'about', 'theirs', 'd', 'what', 'aren', 'shouldn', 'it', 'are', 't', 'i', 'my', 'on', 'there', 'wasn', 'will', 'mustn', 'myself', 'out', 'isn', 'have', 'its', 'through', 'other','a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'did', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'hence', 'here', 'hereafter', 'hereby', 'herein', 'hereupon',  'herself',  'himself', 'his', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the',  'themselves', 'then', 'thence',  'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'thick', 'thin', 'third',  'though', 'three', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'very', 'via', 'was',  'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'the','with', 'within', 'without', 'would', 'yet', 'your', 'yours', 'yourself', 'yourselves'}

####################################
#finding frequency
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

####################################
time = {'today','yesterday','evening','afternoon','morning','tomorrow','tonight','tonite' 'year','day','week','month','monday','tuesday','wednesday','thursday','friday','saturday','sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}
key = []
subj =[]
verb =[]
tell_time =  []
dd = []
data = ''
def tag_data(data):
    global key
    for i in range(len(data)):
        sentences = nltk.sent_tokenize(data[i])
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
        #print(tagged_sentences)
        
        #finding subject, verb and time
        if tagged_sentences:
            ts = tagged_sentences[0]
            j=0

            while j< len(ts):
                if ts[j][0] in time:
                    tell_time.append(ts[j][0])
                    key.append(ts[j][0])
                
                
                elif ts[j][1] == 'NNP' or  ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN':
                    subj.append(ts[j][0])
                    key.append(ts[j][0])
                
                elif ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
                    verb.append(ts[j][0])
                    key.append(ts[j][0])
                j+=1
    #print(key)
    #key = ' '.join(key)
    key = ' '.join(key)
    key = key.lower() 
                
def filter_data(data):
    #removed stopwords - filter_data
    data = [w for w in data.split() if w not in stop_words]
    #print(f_d)
    data = ' '.join(data)
    data = data.split('.') #filter_para
    #print(data)
    #replaced pronoun
    noun = ''
    pr = ''

    for i in range(len(data)):
        data[i] = data[i].split()
        #print (d[i])
        t_s = nltk.pos_tag(data[i])
        #print(t_s)
        for j in range(len(t_s)):
            if t_s[j][1] == 'PRP$' or t_s[j][1] == 'PRP':
                data[i] = [item.replace(t_s[j][0],noun) for item in data[i]]
               
        for j in range(len(t_s)):
            if t_s[j][1] == 'NNP' or t_s[j][1] == 'NNS':
                noun = t_s[j][0]

    #print(data)
    data = [' '.join(w) for w in data]
    return data
    
def open_file():
    global dd
    global data
    file = easygui.fileopenbox()
    #file = 'the_monkey_and_the_wedge.txt'
    with open(file,'r') as file:
        data = file.read()
    data = filter_data(data)
    #print(data)

    tag_data(data)
    #print(subj)
    dd = ''.join(data)


########################################################################################
root = Tk()
root.title('Text processing')
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='light blue')
select_que = IntVar()
#select_que.set(1)
question = [('who',1),("what's going",2),('when',3)]
select_level = IntVar()
level = [('Level 1',1),("Level 2",2),('Level 3',3)]
def ShowChoice():
    #print (select_que.get())
    ab = ''
    if select_que.get() == 1:

        ab = subj
        ab = '\n'.join(ab)
        #print (ab)
        #ht = 50
    elif select_que.get()== 2:
        #print(verb)
        ab = verb
        ab = '\n'.join(ab)
        #ht = 50

    elif select_que.get() == 3:
        ab = tell_time
        ab = '\n'.join(ab)
        #ht = 30
    if ab:
        #whatever_you_do = "Whatever you do will be insignificant,\n but it is very important that you do it.\n(Mahatma Gandhi)"
        text1 = Text(root, height=50, width=20)
        text1.grid(row = 6, column = 0)
        text1.configure( font=('Arial', 14, 'bold', ))

        text1.insert(END,ab)

def show_keyword():
    global key
    #print(key)
    l = 0
    flag = 0
    k = []
    dictionary = wordListToFreqDict(key.split())
    sort_dict = sortFreqDict(dictionary)
    if select_level.get() == 1:
        l = 0
        flag = 1
    if select_level.get() == 2:
        l = 10
        flag = 1
    if select_level.get() == 3:
        l = 20
        flag = 1
    if flag == 1:
        for s in sort_dict[l:l+10]:
            k.append(s[1])
        k = '\n'.join(k)
        text2 = Text(root, height=50, width=20)
        text2.grid(row = 6, column = 1)
        text2.configure( font=('Arial', 14, 'bold'))
        text2.insert(END,k)
  
def show_user_key():
    #print(enter_key.get())
    
    global dd
    global data
    #dd = ''.join(data)
    dd = dd.lower()
    store = []
    #print(data)
    flag = 0
    k = []
    userkey = enter_key.get()
    userkey=userkey.lower()

    if userkey not in dd.split():
        #print('finding synonyms')
        synonyms = []
        for syn in wordnet.synsets(userkey):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())

        #print (synonyms)
        for syn in synonyms:
            
            if flag == 0 and syn in dd.split():
                flag = 1
                #print (syn)
                userkey = syn

                

    for i in range(len(data)):
        #print(data[i])
        if userkey in data[i].lower():
            store.append(data[i])
            store.append(data[i+1])
            if i>1:
                store.append(data[i-1])

    #print(store)
              
    ###################################################

    #print('=' *40)
    #print('\nSentences related to your keyword: \n')
    #print(store)

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
    l = 0
    for s in sort_dict:
            k.append(s[1])
    k = '\n'.join(k)
    text2 = Text(root, height=50, width=15)
    text2.grid(row = 6, column = 2)
    text2.configure( font=('Arial', 14, 'bold'))
    text2.insert(END,k)
    '''
    #print('\nRelated keywords: ')
    #print()
    l = 0
    more = 'y'
    while l<len(sort_dict) and (more == 'y' or more == 'Y'):
        #l = l+10
        for s in sort_dict[l:l+10]:
            print(str(s))
        print()
        more = input('Want to know more(y/n) ')
        l = l+10
    '''

#========row = 0,1 ===========================================

Button(root, text='Select File', command=open_file, font = "Helvetica 16 bold italic").grid(row=1,column = 1, pady=4)

#========== row = 2 ==============================================
Button(root, text='Ask question',font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 0, pady=4)
Button(root, text='  Keyword  ',command=show_keyword,font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 1,padx=300 ,pady=4)
Button(root, text='  Your Keyword    ',
       font = "Helvetica 16 bold italic", bg = "light green").grid(row=2,column = 2, pady=4)

#======= row = 2 , col = 0========================================
for txt, val in question:
    Radiobutton(root, 
                text=txt,
                indicatoron = 0,
                width = 20,
                padx = 20,
                #pady = 20,
                variable=select_que, 
                command=ShowChoice,
                value=val,font = "Helvetica 16 bold italic",bg = "yellow").grid(row=2+val,column = 0, pady=4)

#======= row = 2 , col = 1========================================
for txt, val in level:
    Radiobutton(root, 
                text=txt,
                indicatoron = 0,
                width = 20,
                padx = 20,
                #pady = 20,
                variable=select_level, 
                command=show_keyword,
                value=val,font = "Helvetica 16 bold italic",bg = "yellow").grid(row=2+val,column = 1, pady=4)
#========= col = 2, ask-keyword=============================

enter_key = Entry(root)
enter_key.grid(row =3 ,column = 2)
#enter_key.bind("<Return>")
Button(root, text='  Search    ',command = show_user_key,
       font = "Helvetica 12 bold italic", bg = "light green").grid(row=4,column = 2, pady=4)


root.mainloop()
#########################################################################################
