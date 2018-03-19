import nltk
import easygui
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from collections import Counter
lemma = WordNetLemmatizer()
from tkinter import *

### global variables ##############

stop_words = {'Once','\'','A','|','but','Regularly','time','regularly','till','this','This','There','As','Since','In','got','But','lot','there','A','a','against','The', 'in', ',' ,'.',  '! ', 'to', 'because', 'couldn', 'should', 'was', 'who', 'doesn', 'itself', 'has', 'below', 'were', 'each', 'before', 'while', 'from', 'hasn', 'hers', 'off', 'when', 'ma', 'both', 'which', 'here', 'can', 'over', 'further', 'not', 'these', 'now', 'shan', 'ourselves', 'no', 'whom', 'of', 'under', 'then', 'few', 'had', 'so', 'do', 'the', 'does', 'didn', 'their', 'if', 'mightn', 'how', 've', 'hadn', 'once', 'into', 'been', 'more', 'those', 'y', 'am', 'weren', 'too', 're', 'an', 'after', 'with', 'our', 's', 'at', 'why', 'only', 'your', 'again', 'wouldn', 'a', 'all', 'm', 'very', 'by', 'herself', 'having', 'and', 'is', 'as', 'some', 'needn', 'be', 'or', 'yourself', 'ours', 'yours', 'being', 'any', 'll', 'o', 'for', 'above', 'up', 'yourselves', 'ain', 'haven', 'down', 'doing', 'did', 'won', 'that',  'between', 'same', 'she', 'such', 'but', 'most', 'own', 'don', 'than', 'during', 'themselves', 'nor', 'just', 'until', 'where', 'them', 'about', 'theirs', 'd', 'what', 'aren', 'shouldn',  'are', 't', 'i', 'my', 'on', 'there', 'wasn', 'will', 'mustn', 'myself', 'out', 'isn', 'have', 'its', 'through', 'other','a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'did', 'do', ' done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'hence', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'It',  'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once',  'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the',  'themselves', 'then', 'thence',  'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'thick', 'thin', 'third',  'though', 'three', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'very', 'via', 'was',  'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'the','with', 'within', 'without', 'would', 'yet', 'your', 'yours', 'yourself', 'yourselves'}
time = {'today','yesterday','evening','afternoon','morning','tomorrow','tonight','tonite' 'year','day','week','month','monday','tuesday','wednesday','thursday','friday','saturday','sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}


verb = []

tell_time =  []

data = ''
mid_strong_noun = []
mid_weak_noun = []
section_strong_noun = []
section_weak_noun = []
section_data = []
mid_data = []
sorted_noun = []

find_sorted_key = []
sorted_verb = []
sorted_key = []

####################################
#finding frequency
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    #print(wordfreq)
    #print(wordfreq)
    return dict(zip(wordlist,wordfreq))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

####################################
def compute_all():
    #noun sorting
    global sorted_noun
    global sorted_verb
    global sorted_key
     
    
    dict_section_strong_noun = wordListToFreqDict(section_strong_noun)
    for k in dict_section_strong_noun:
        dict_section_strong_noun[k] *= 0.8
    
    dict_section_weak_noun = wordListToFreqDict(section_weak_noun)
    for k in dict_section_weak_noun:
        dict_section_weak_noun[k] *= 0.4
      
    dict_mid_strong_noun = wordListToFreqDict(mid_strong_noun)
    for k in dict_mid_strong_noun:
        dict_mid_strong_noun[k] *= 0.7
                           
    dict_mid_weak_noun = wordListToFreqDict(mid_weak_noun)
    for k in dict_mid_weak_noun:
        dict_mid_weak_noun[k] *= 0.3
                          
    A = Counter(dict_section_strong_noun)
    B = Counter(dict_section_weak_noun)
    C = Counter(dict_mid_strong_noun)
    D = Counter(dict_mid_weak_noun)
    
    sorted_noun = list(A+B+C+D)
    
    #=========================================
    #sorting verb:
    v= wordListToFreqDict(verb)
    sorted_verb = sortFreqDict(v)
    
    #==========================================
    #sorting key:
    for k in v:
        v[k] *= 0.5
    E = Counter(v)
    sorted_key = list(A+B+C+D+E)
        
    
######################################################################   
def tag_mid_data(mid_data):
    #global key     #for keyword
    #global subj    # for noun list (find subject)
    global verb    # for verb list
    global mid_strong_noun
    global mid_weak_noun

    for i in range(len(mid_data)):
        sentences = nltk.sent_tokenize(mid_data[i])
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        
        print(tagged_sentences)
        
        #finding subject, verb and time
        if tagged_sentences:
            ts = tagged_sentences[0]
            j=0
            flag_strong_noun = 0
            while j< len(ts):
                
                if ts[j][0] in time:
                    tell_time.append(ts[j][0])

                elif ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
                    t = lemma.lemmatize(ts[j][0],pos ='v')
                    verb.append(t)
                    
                elif ts[j][1] == 'NNP' or  ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN':
                    t = lemma.lemmatize(ts[j][0],pos ='n')
                    if flag_strong_noun == 0:
                            mid_strong_noun.append(t)
                            flag_strong_noun = 1
                    else:
                            mid_weak_noun.append(t)

                j+=1
    mid_weak_noun = [w for w in mid_weak_noun if w not in stop_words]
    mid_strong_noun = [w for w in mid_strong_noun if w not in stop_words] 
    verb = [w.lower() for w in verb if w not in stop_words]

    #print('mid_weak_noun: ',mid_weak_noun)
    #print('mid_strong_noun: ',mid_strong_noun)
    #print('verb @ mid: ',verb)
    
####################################################################

def tag_section_data(section_data):
    #global key     #for keyword
    #global subj    # for noun list (find subject)
    global verb    # for verb list
    global section_strong_noun
    global section_weak_noun

    for i in range(len(section_data)):
        sentences = nltk.sent_tokenize(section_data[i])
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        
        print(tagged_sentences)
        
        #finding subject, verb and time
        if tagged_sentences:
            ts = tagged_sentences[0]
            j=0
            flag_strong_noun = 0
            while j< len(ts):
                
                if ts[j][0] in time:
                    tell_time.append(ts[j][0])

                elif ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
                    t = lemma.lemmatize(ts[j][0],pos ='v')
                    verb.append(t)
                
                elif ts[j][1] == 'NNP' or  ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN':
                    t = lemma.lemmatize(ts[j][0],pos ='n')
                    if flag_strong_noun == 0:
                            section_strong_noun.append(t)
                            flag_strong_noun = 1
                    else:
                            section_weak_noun.append(t)

                j+=1
    section_weak_noun = [w.lower() for w in section_weak_noun if w not in stop_words]
    section_strong_noun = [w.lower() for w in section_strong_noun if w not in stop_words]
    verb = [w.lower() for w in verb if w not in stop_words]

    #print('mid_weak_noun: ',section_weak_noun)
    #print('verb: ',verb)
  
    
####################################################################
def remove_pronoun(data): #replace pronoun with noun

    
    #data = data.split('.') #filter_para
    noun = ['']
    #print('data in remove-pronoun: ', data)
    #print(len(data))
    for i in range(len(data)):
        data[i] = data[i].split()
        #print('data[i]: ',data[i])
        t_s = nltk.pos_tag(data[i])
        prep_count = 0
        #print('t_s: ',t_s)
        #print(t_s)
        for j in range(len(t_s)):
            #print(len(t_s))
            if prep_count == len(noun):
                prep_count = 0
            
            if t_s[j][1] == 'PRP$' or t_s[j][1] == 'PRP':
                data[i] = [item.replace(t_s[j][0],noun[prep_count]) for item in data[i]]
                prep_count+=1
                
        #noun = []
        flag_noun = 0
        for j in range(len(t_s)):
            if  t_s[j][0] not in time and(t_s[j][1] == 'NNP' or t_s[j][1] == 'NNS'or t_s[j][1] =='NNPS' or t_s[j][1] == 'NN') :
                if flag_noun == 0:
                    noun = []
                    flag_noun =1
                noun.append(t_s[j][0])
   

    data = [' '.join(w) for w in data]

    return data

#################################################
# fetching data from user's given file
def open_file():
    
    global data
    global section_data
    global mid_data
    
    #to display file name on the screen
    file = easygui.fileopenbox()
    #file = 'the_monkey_and_the_wedge.txt'

    disp_file1 = Text(root, height = 1, width = 60)
    disp_file1.grid(row = 1, column = 1, columnspan =3)
    disp_file1.configure( font=('Arial', 14))
    disp_file1.insert(END,file)
    
    #open file and read the text and store it in data string
    with open(file,'r') as f:
       data = f.read()
    
    d = data.split('\n')
    
    section_data = d[0] + d[-1]
    section_data  = section_data.split('.')
    
    mid_data = d[1: len(d)-1]
    mid_data = ' '.join(mid_data)
    mid_data  = mid_data.split('.')

    #remoing the pronouns with noun in the data
    section_data = remove_pronoun(section_data)
    mid_data = remove_pronoun(mid_data)


    #cleaning data
    data = data.replace(',','').replace(':','').replace('"','').replace('\'','').replace('?','')
    
    tag_mid_data(mid_data)
    tag_section_data(section_data)
    compute_all()
    #find_verb(section_data, section_strong_noun)
    
#################################################

  
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

def more_who_ques():
    k = sorted_noun[18:]
    ab = '\n'.join(k)

    text2 = Text(root, height=18, width=20)
    text2.grid(row = 6, column = 0)
    text2.configure( font=('Arial', 14, 'bold'))
    text2.insert(END,ab)    

def more_what_ques():

    k = sorted_verb[18:]
    k = str(k)
    k = ' '+k
    k = k.replace('),',')\n')
    k = k.replace('[','').replace(']','')
    ab = k
    
    text2 = Text(root, height=18, width=20)
    text2.grid(row = 6, column = 0)
    text2.configure( font=('Arial', 14, 'bold'))
    text2.insert(END,ab)

    
    
def ShowChoice():

    ab = ''
    if select_que.get() == 1:

        k = sorted_noun[:18]
        ab = '\n'.join(k)

    elif select_que.get()== 2:
       
        k = sorted_verb[:18]
        k = str(k)
        k = ' '+k
        k = k.replace('),',')\n')
        k = k.replace('[','').replace(']','')
        ab = k

    elif select_que.get() == 3:
        ab = tell_time
        ab = '\n'.join(ab)
        #ht = 30
    if ab:
        text1 = Text(root, height=18, width=20)
        text1.grid(row = 6, column = 0)
        text1.configure( font=('Arial', 14, 'bold', ))

        text1.insert(END,ab)
        if select_que.get() == 1 and len(sorted_noun)>18:
            Button(root, text=' More   ',command = more_who_ques,font = "Helvetica 12 bold italic", bg = "light green").grid(row=15,column = 0, pady=4)
        if select_que.get() == 2 :
            #print('hi')
            Button(root, text='  Search    ',command = more_what_ques,font = "Helvetica 12 bold italic", bg = "light green").grid(row=15,column = 0, pady=4)

          


def show_keyword():
    global key
    #print(key)
    l = 0
    flag = 0
    k = []
    
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

        k = sorted_key[l:l+10]
        k = '\n'.join(k)
        text2 = Text(root, width=20, height = 10)
        text2.grid(row = 6, column = select_level.get())
        text2.configure( font=('Arial', 14, 'bold'))
        text2.insert(END,k)


def more_user_key():
    #print ('hi') 
    kk = find_sorted_key[15: ]
    #print(k)
    kk = '\n'.join(kk)
    text2 = Text(root, height=15, width=15)
    text2.grid(row = 6, column = 4)
    text2.configure( font=('Arial', 14, 'bold'))
    text2.insert(END,kk)
    
def show_user_key():
    global find_sorted_key
    dd = section_data + mid_data
    dd = str(dd)
    dd = dd.lower()
    d = dd
    d = d.split('.')
    #print('dd: ',dd)
    store = []
    #print(data)
    flag = 0
    #k = []
    userkey = enter_key.get()
    userkey=userkey.lower()
    #print('userkey', userkey)
    #print('dd.split()', dd.split())
    if userkey not in dd.split():
        synonyms = []
        for syn in wordnet.synsets(userkey):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())

        for syn in synonyms:
            
            if flag == 0 and syn in dd.split():
                flag = 1
                userkey = syn

                

    for i in range(len(d)):
        #print(data[i])
        if userkey in d[i]:
            #print(d[i])
            store.append(d[i])
            #if (i+1) <len(d):
            #    store.append(d[i+1])
            #if i>1:
            #    store.append(d[i-1])

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
        #chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
        #print(tagged_sentences)

        
        #finding subject, verb and object
        if tagged_sentences:
            ts = tagged_sentences[0]
            j=0

            while j< len(ts):

                if ts[j][1] == 'NNP' or ts[j][1] == 'PRP' or ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN'or ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
                    rel_key.append(ts[j][0])
                j+=1


        
    
    rk = [w.lower() for w in rel_key if w not in stop_words]
    #rk = ' '.join(rk)
    dictionary = wordListToFreqDict(rk)
    sortkey = sortFreqDict(dictionary)
   
    for s in sortkey:
            find_sorted_key.append(s[1])
    kk = find_sorted_key[:15]
    kk = '\n'.join(kk)
    text2 = Text(root, height=15, width=15)
    text2.grid(row = 6, column = 4)
    text2.configure( font=('Arial', 14, 'bold'))
    text2.insert(END,kk)
        
    if len(find_sorted_key)>15:
        Button(root, text='  Search    ',command = more_user_key,font = "Helvetica 12 bold italic", bg = "light green").grid(row=15,column = 4, pady=4)



#========row = 0,1 ===========================================

Button(root, text='Select File', command=open_file, font = "Helvetica 16 bold italic").grid(row=0,column = 1, pady=4, columnspan =3 )
disp_file = Text(root, height = 1, width = 60)
disp_file.grid(row = 1, column = 1, columnspan =3)
disp_file.configure( font=('Arial', 14))

#========== row = 2 ==============================================
Button(root, text='Ask question',font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 0, pady=4)
Button(root, text='  keyword ',command=show_keyword,font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 1,padx=300 ,pady=4, columnspan =3)
Button(root, text='  Your Keyword    ',
       font = "Helvetica 16 bold italic", bg = "light green").grid(row=2,column = 4, pady=4, padx = 20)

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
                width = 10,
                padx = 30,
                #pady = 20,
                variable=select_level, 
                command=show_keyword,
                value=val,font = "Helvetica 16 bold italic",bg = "yellow").grid(row=3,column = val, pady=4)
#========= col = 2, ask-keyword=============================

enter_key = Entry(root)
enter_key.grid(row =3 ,column = 4)
#enter_key.bind("<Return>")
Button(root, text='  Search    ',command = show_user_key,
       font = "Helvetica 12 bold italic", bg = "light green").grid(row=4,column = 4, pady=4)


root.mainloop()
#########################################################################################
