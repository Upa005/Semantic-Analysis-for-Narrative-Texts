# Calculation is according to percentage only
import nltk
import easygui
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from collections import Counter
lemma = WordNetLemmatizer()
from tkinter import *

### global variables ##############

stop_words = {'O','aah','Ah','Once','\'','A','\'s','|','but','Regularly','time','regularly','till','this','This','There','As','Since','In','got','But','lot','there','A','a','against','The', 'in', ',' ,'.',  '! ', 'to', 'because', 'couldn', 'should', 'was', 'who', 'doesn', 'itself', 'has', 'below', 'were', 'each', 'before', 'while', 'from', 'hasn', 'hers', 'off', 'when', 'ma', 'both', 'which', 'here', 'can', 'over', 'further', 'not', 'these', 'now', 'shan', 'ourselves', 'no', 'whom', 'of', 'under', 'then', 'few', 'had', 'so', 'do', 'the', 'does', 'didn', 'their', 'if', 'mightn', 'how', 've', 'hadn', 'once', 'into', 'been', 'more', 'those', 'y', 'am', 'weren', 'too', 're', 'an', 'after', 'with', 'our', 's', 'at', 'why', 'only', 'your', 'again', 'wouldn', 'a', 'all', 'm', 'very', 'by', 'herself', 'having', 'and', 'is', 'as', 'some', 'needn', 'be', 'or', 'yourself', 'ours', 'yours', 'being', 'any', 'll', 'o', 'for', 'above', 'up', 'yourselves', 'ain', 'haven', 'down', 'doing', 'did', 'won', 'that',  'between', 'same', 'she', 'such', 'but', 'most', 'own', 'don', 'than', 'during', 'themselves', 'nor', 'just', 'until', 'where', 'them', 'about', 'theirs', 'd', 'what', 'aren', 'shouldn',  'are', 't', 'i', 'my', 'on', 'there', 'wasn', 'will', 'mustn', 'myself', 'out', 'isn', 'have', 'its', 'through', 'other','a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'did', 'do', ' done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'hence', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'It',  'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once',  'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the',  'themselves', 'then', 'thence',  'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'thick', 'thin', 'third',  'though', 'three', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'very', 'via', 'was',  'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'the','with', 'within', 'without', 'would', 'yet', 'your', 'yours', 'yourself', 'yourselves'}


verb = []

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

percent_weak_noun1 = []
percent_strong_noun1 = []
percent_verb1 = []

percent_weak_noun2 = []
percent_strong_noun2 = []
percent_verb2 = []

percent_weak_noun3 = []
percent_strong_noun3 = []
percent_verb3 = []

percent_sorted_noun = []
percent_sorted_verb  = []
percent_sorted_key = []
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
        
        #print(tagged_sentences)
        
        #finding subject, verb and time
        if tagged_sentences:
            ts = tagged_sentences[0]
            j=0
            flag_strong_noun = 0
            while j< len(ts):
                
     

                if ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
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
    mid_weak_noun = [w.lower() for w in mid_weak_noun if w not in stop_words]
    mid_strong_noun = [w.lower() for w in mid_strong_noun if w not in stop_words] 
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
        
        #datprint(tagged_sentences)
        
        #finding subject, verb and time
        if tagged_sentences:
            ts = tagged_sentences[0]
            j=0
            flag_strong_noun = 0
            while j< len(ts):

                if ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
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
    #print('Inside remove pronoun: ')
    for i in range(len(data)):
        #print('Initial data: ',data[i])
        data[i] = data[i].split()
        #print('data[i]: ',data[i])
        t_s = nltk.pos_tag(data[i])
        prep_count = 0
        
        #print('t_s: ',t_s)
        #print(t_s)
        for j in range(len(t_s)):
            
            if prep_count == len(noun):
                prep_count = 0
            
            if t_s[j][1]  == 'PRP$' or t_s[j][1]  == 'PRP':
                #print(j)
                data[i][j] = noun[prep_count]
                #data[i] = [item.replace(j[0],noun[prep_count],1) for item in data[i]]
                prep_count+=1
                
        #noun = []
        flag_noun = 0
        for j in range(len(t_s)):
            if  (t_s[j][1] == 'NNP' or t_s[j][1] == 'NNS'or t_s[j][1] =='NNPS' or t_s[j][1] == 'NN') :
                if flag_noun == 0:
                    noun = []
                    flag_noun =1
                noun.append(t_s[j][0])
   
        #print('Changded: ',data[i],'\n')
    data = [' '.join(w) for w in data]
    
    #print("+"*60)
    return data

#################################################

def paragraph():
    d = data.split('\n')
    
    section_data = d[1] + d[-1]
    section_data  = section_data.split('.')
    
    mid_data = d[2: len(d)-1]
    mid_data = ' '.join(mid_data)
    mid_data  = mid_data.split('.')

    #remoing the pronouns with noun in the data
    section_data = remove_pronoun(section_data)
    mid_data = remove_pronoun(mid_data)


    #cleaning data
    #data = data.replace(',','').replace(':','').replace('"','').replace('\'','').replace('?','')
    
    tag_mid_data(mid_data)
    tag_section_data(section_data)
    compute_all()
###############################################
def percentage_compute_all():
    #noun sorting
    global sorted_noun
    global sorted_verb
    global sorted_key
    
    sorted_key = []
    #print(sec1_strong_noun_val.get())  
    
    dict_percent_strong_noun1 = wordListToFreqDict(percent_strong_noun1)
    #print(percent_strong_noun1)
    #print("=")
    #print(dict_percent_strong_noun1)
    for k in dict_percent_strong_noun1:
        dict_percent_strong_noun1[k] *= float(sec1_strong_noun_val.get())
    #print(dict_percent_strong_noun1)
    
    dict_percent_weak_noun1 = wordListToFreqDict(percent_weak_noun1)
    for k in dict_percent_weak_noun1:
        dict_percent_weak_noun1[k] *= float(sec1_weak_noun_val.get()) 
    ################
               
    dict_percent_strong_noun2 = wordListToFreqDict(percent_strong_noun2)
    for k in dict_percent_strong_noun2:
        dict_percent_strong_noun2[k] *= float(sec2_strong_noun_val.get())
    
    dict_percent_weak_noun2 = wordListToFreqDict(percent_weak_noun2)
    for k in dict_percent_weak_noun2:
        dict_percent_weak_noun2[k] *= float(sec2_weak_noun_val.get())
     ##############
                          
    dict_percent_strong_noun3 = wordListToFreqDict(percent_strong_noun3)
    for k in dict_percent_strong_noun3:
        dict_percent_strong_noun3[k] *= float(sec3_strong_noun_val.get())
    
    dict_percent_weak_noun3 = wordListToFreqDict(percent_weak_noun3)
    for k in dict_percent_weak_noun3:
        dict_percent_weak_noun3[k] *= float(sec3_weak_noun_val.get())
     ##################
    #print('\n\nsect 3 weak noun: ',dict_percent_strong_noun3)
                          
    A = Counter(dict_percent_strong_noun1)
    s = A
    s1 = A
    #print('s1',s1)
    B = Counter(dict_percent_strong_noun2)
    s.update(B)
    s2 = B
    
    
    C = Counter(dict_percent_strong_noun3)
    s.update(C)
    s3 = C
    D = Counter(dict_percent_weak_noun1)
    s.update(D)
    ##########################
    #s1.update(D)
    #print('D:',D)
    #print('s1:',s1)
    print("==" *60)
    print('\nSection 1: ')
    print('Strong noun: ', dict_percent_strong_noun1)
    print('\nWeak noun  : ',dict_percent_weak_noun1)
    print('\nVerb: ',percent_verb1)

    print()
    #print(' noun  list: ',s1)   
    #############################

    E = Counter(dict_percent_weak_noun2) 
    s.update(E)
    s2.update(E)
    
    print("==" *60)
    print('\nSection 2:')
    print('Strong noun: ', dict_percent_strong_noun2)
    print('\nWeak noun  : ',dict_percent_weak_noun2)
    print('\nVerb: ',percent_verb2)
    print()
    #print('noun list: ',s2)
    F = Counter(dict_percent_weak_noun3)
    s.update(F)
    s3.update(F)
    #####################
    print("==" *60)
    print('\nSection 3:')
    print('Strong noun: ', dict_percent_strong_noun3)
    print('\nWeak noun  : ',dict_percent_weak_noun3)
    print('\nVerb: ',percent_verb3)

    print()
    #print('noun list: ',s3)
    #############################
    #G = Counter(dict_percent_weak_noun1)
    #s.update(G)
    
    

    sorted_noun=sorted(s.items(), key=lambda x: x[1],reverse = True) 
    print()
    print('=='*60)
    print('sorted_noun: ',sorted_noun)
    sorted_noun = list(sorted_noun)
    
    #print()
    #print('s: ',s)
    #print('\nsorted noun: ',sorted_noun)
    
    #print('float(sec3_weak_noun_val.get())',float(sec3_weak_noun_val.get()))
    
    #=========================================
    #sorting verb:
    p_v = percent_verb1 + percent_verb2 + percent_verb3
    v= wordListToFreqDict(p_v)
    sorted_verb = sortFreqDict(v)
    
    #==========================================
    #sorting key:
    for k in v:
        v[k] *= 0.7
    H = Counter(v)
    hh = s
    hh.update(H)
    s_k =sorted(hh.items(), key=lambda x: x[1],reverse = True)  
    s_k = list(s_k)
    for i in s_k:
        sorted_key.append(i[0])
    #print('s_k',s_k)
    #print('\n\nsorted_key ',s_k)
    
    #sorted_noun = list(sorted_noun)
    
    
    
def tag_percentage(data):
    
    percent_strong_noun = []
    percent_weak_noun = []
    percent_verb = []
    
    for i in range(len(data)):
        sentences = nltk.sent_tokenize(data[i])
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        
        #datprint(tagged_sentences)
        
        #finding subject, verb and time
        if tagged_sentences:
            ts = tagged_sentences[0]
            j=0
            flag_strong_noun = 0
            while j< len(ts):

                if ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG':
                    t = lemma.lemmatize(ts[j][0],pos ='v')
                    percent_verb.append(t)
                
                elif ts[j][1] == 'NNP' or  ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN':
                    t = lemma.lemmatize(ts[j][0],pos ='n')
                    if flag_strong_noun == 0:
                            percent_strong_noun.append(t)
                            flag_strong_noun = 1
                    else:
                            percent_weak_noun.append(t)

                j+=1
    percent_weak_noun = [w.lower() for w in percent_weak_noun if w not in stop_words]
    percent_strong_noun = [w.lower() for w in percent_strong_noun if w not in stop_words]
    percent_verb = [w.lower() for w in percent_verb if w not in stop_words]
    
    return [percent_weak_noun,percent_strong_noun,percent_verb]

def percentage():
    
    global percent_weak_noun1
    global percent_strong_noun1 
    global percent_verb1 
    
    global percent_weak_noun2 
    global percent_strong_noun2 
    global percent_verb2 
    
    global percent_weak_noun3 
    global percent_strong_noun3 
    global percent_verb3 
    
    d = data.split()
    l = len(d)
    
    sec1 = d[:int(0.30*l)]
    sec2 = d[int(0.30*l):int(0.60*l)]
    sec3 = d[int(0.60*l):]
     
    print(sec1)
    print('\n',sec2)
    print('\n',sec3)
    sec1 = ' '.join(sec1)
    sec1  = sec1.split('.')
    sec1 = remove_pronoun(sec1)
    

    
    sec2 = ' '.join(sec2)
    sec2  = sec2.split('.')
    sec2 = remove_pronoun(sec2)
    
    sec3 = ' '.join(sec3)
    sec3  = sec3.split('.')
    sec3 = remove_pronoun(sec3)
    
    percent_weak_noun1,percent_strong_noun1,percent_verb1 = tag_percentage(sec1)
    #print(sec1)
    #print('percent_weak_noun,percent_strong_noun,percent_verb',percent_weak_noun1,percent_strong_noun1,percent_verb1)
   
    percent_weak_noun2,percent_strong_noun2,percent_verb2 = tag_percentage(sec2)
    #print('percent_weak_noun,percent_strong_noun,percent_verb',percent_weak_noun2,percent_strong_noun2,percent_verb2)
    
    percent_weak_noun3,percent_strong_noun3,percent_verb3 = tag_percentage(sec3)
    #print('percent_weak_noun,percent_strong_noun,percent_verb',percent_weak_noun3,percent_strong_noun3,percent_verb3)

    percentage_compute_all()
################################################
# fetching data from user's given file

def open_file():
    global dd
    global data

    global key 
    global subj
    global verb
    global tell_time
    global strong_noun 
    global weak_noun 
    global dictionary 
    global k    
    global mid_strong_noun
    global mid_weak_noun
    global section_strong_noun
    global section_weak_noun 
    global section_data 
    global mid_data
    global sorted_noun
    global find_sorted_key 
    global sorted_verb 
    global sorted_key 
    
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
    data = ''
    
    key = []
    subj =[]
    verb = []
    dd = []
    strong_noun = []
    weak_noun = []
    dictionary = []
    k=[]
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
                
    percentage()
    
#################################################

  
########################################################################################
root = Tk()
v= IntVar()
root.title('Text processing')
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='light blue')
select_que = IntVar()
sec1_strong_noun_val = IntVar()
question = [('who',1),("what's going",2)]
select_level = IntVar()
level = [('Level 1',1),("Level 2",2),('Level 3',3)]

def more_who_ques():
    k = sorted_noun[18:]
    ab = '\n'.join(k)

    text2 = Text(root, height=18, width=20)
    text2.grid(row = 6, column = 0,rowspan = 10)
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
    text2.grid(row = 6, column = 0,rowspan = 10)
    text2.configure( font=('Arial', 14, 'bold'))
    text2.insert(END,ab)

    
    
def ShowChoice():

    ab = ''
    if select_que.get() == 1:
        t = []
        for i in sorted_noun:
            t.append(i[0    ])
        k = t[:18]
        #print('k is; ',k)
        ab = '\n'.join(k)

    elif select_que.get()== 2:
       
        k = sorted_verb[:18]
        #print(k)
        k = str(k)
        k = ' '+k
        k = k.replace('),',')\n')
        k = k.replace('[','').replace(']','')
        ab = k

   
    if ab:
        text1 = Text(root, height=18, width=20 )
        text1.grid(row = 5, column = 0,rowspan = 10)
        text1.configure( font=('Arial', 14, 'bold', ))

        text1.insert(END,ab)
        if select_que.get() == 1 and len(sorted_noun)>18:
            Button(root, text=' More   ',command = more_who_ques,font = "Helvetica 12 bold italic", bg = "light green").grid(row=15,column = 0, pady=4)
        if select_que.get() == 2 :
            Button(root, text='  More   ',command = more_what_ques,font = "Helvetica 12 bold italic", bg = "light green").grid(row=15,column = 0, pady=4)

          


def show_keyword():
    global key
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
        text2.grid(row = 5, column = select_level.get(),rowspan = 10)
        text2.configure( font=('Arial', 14, 'bold'))
        text2.insert(END,k)


def more_user_key():
    kk = find_sorted_key[15: ]
    kk = '\n'.join(kk)
    text2 = Text(root, height=15, width=15)
    text2.grid(row = 5, column = 4,rowpan = 10)
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
        if userkey in d[i]:
            store.append(d[i])


    rel_key = []
    for i in range(len(store)):
        
        #tagging the words
        sentence = store[i]
        word = sentence
        sentences = nltk.sent_tokenize(word)
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
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
    dictionary = wordListToFreqDict(rk)
    sortkey = sortFreqDict(dictionary)
   
    for s in sortkey:
            find_sorted_key.append(s[1])
    kk = find_sorted_key[:15]
    kk = '\n'.join(kk)
    text2 = Text(root, height=15, width=15)
    text2.grid(row = 5, column = 4)
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
Button(root, text='Ask Questions',font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 0, pady=4)

Button(root, text='  Percentage ',command=show_keyword,font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 1,padx=300 ,pady=4, columnspan =3)
#Button(root, text='  paragraph ',command=paragraph,font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 0,padx=300 ,pady=4, columnspan =3)
#Button(root, text='  percentage',command=percentage,font = "Helvetica 16 bold italic",bg = "light green").grid(row=2,column = 2,padx=300 ,pady=4, columnspan =3)
Button(root, text='  Strength  ',
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

#enter_key = Entry(root)
#enter_key.grid(row =3 ,column = 4)
#Button(root, text='  Search    ',command = show_user_key,
#       font = "Helvetica 12 bold italic", bg = "light green").grid(row=4,column = 4, pady=4)
############
Button(root, text=' Section 1 ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=3,column = 4, pady=4,columnspan = 2 )
Button(root, text=' Srong Noun ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=4,column = 4, pady=4, )
Button(root, text=' Weak Noun ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=5,column = 4, pady=4 )

Button(root, text=' Section 2' ,font = "Helvetica 12 bold italic", bg = "light green").grid(row=6,column = 4, pady=4,columnspan = 2 )
Button(root, text=' Srong Noun ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=7,column = 4, pady=4 )
Button(root, text=' Weak Noun ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=8,column = 4, pady=4 )

Button(root, text=' Section 3 ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=9,column = 4, pady=4,columnspan = 2 )
Button(root, text=' Srong Noun ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=10,column = 4, pady=4)
Button(root, text=' Weak Noun ',font = "Helvetica 12 bold italic", bg = "light green").grid(row=11,column = 4, pady=4 )


sec1_strong_noun_val = Entry(root)
sec1_strong_noun_val.grid(row =4 ,column = 5)
sec1_strong_noun_val.insert(0,'0.8')
#v.set(0.8)

sec1_weak_noun_val = Entry(root)
sec1_weak_noun_val.grid(row =5 ,column = 5)
sec1_weak_noun_val.insert(0,'0.2')

sec2_strong_noun_val = Entry(root)
sec2_strong_noun_val.grid(row =7 ,column = 5)
sec2_strong_noun_val.insert(0,'0.6')

sec2_weak_noun_val = Entry(root)
sec2_weak_noun_val.grid(row =8 ,column = 5)
sec2_weak_noun_val.insert(0,'0.4')

sec3_strong_noun_val = Entry(root)
sec3_strong_noun_val.grid(row =10 ,column = 5)
sec3_strong_noun_val.insert(0,'0.8')

sec3_weak_noun_val = Entry(root)
sec3_weak_noun_val.grid(row =11 ,column = 5)
sec3_weak_noun_val.insert(0,'0.2')

Button(root, text=' Evaluate ',command = percentage_compute_all,font = "Helvetica 12 bold italic", bg = "light green").grid(row=12,column = 4, pady=4, columnspan = 2 )


root.mainloop()
#########################################################################################
