#answer wh questions in a paragraph
import nltk
import nltk.data
from nltk.tokenize import word_tokenize
import easygui

stop_words = {'against', 'in', ',' ,'.',  '! ', 'to', 'because', 'couldn', 'should', 'was', 'who', 'doesn', 'itself', 'has', 'below', 'were', 'each', 'before', 'while', 'from', 'hasn', 'hers', 'off', 'when', 'ma', 'both', 'which', 'his', 'here', 'can', 'over', 'further', 'not', 'these', 'now', 'shan', 'ourselves', 'no', 'whom', 'of', 'under', 'then', 'few', 'had', 'so', 'do', 'the', 'does', 'didn', 'their', 'if', 'mightn', 'how', 've', 'hadn', 'once', 'into', 'been', 'more', 'those', 'y', 'am', 'weren', 'too', 're', 'an', 'after', 'with', 'our', 's', 'at', 'why', 'only', 'your', 'again', 'wouldn', 'a', 'all', 'm', 'very', 'by', 'herself', 'having', 'and', 'is', 'as', 'some', 'needn', 'be', 'or', 'yourself', 'ours', 'yours', 'being', 'any', 'll', 'o', 'for', 'above', 'up', 'yourselves', 'ain', 'haven', 'down', 'doing', 'did', 'won', 'that', 'himself', 'between', 'same', 'she', 'such', 'this', 'but', 'most', 'own', 'don', 'than', 'during', 'themselves', 'nor', 'just', 'until', 'where', 'them', 'about', 'theirs', 'd', 'what', 'aren', 'shouldn', 'it', 'are', 't', 'i', 'my', 'on', 'there', 'wasn', 'will', 'mustn', 'myself', 'out', 'isn', 'have', 'its', 'through', 'other', 'we'}
time = {'today','yesterday','evening','afternoon','morning','tomorrow','tonight','tonite' 'year','day','week','month','monday','tuesday','wednesday','thursday','friday','saturday','sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}


repeat_question = 'y'
file = easygui.fileopenbox()
with open(file,'r') as file:
    data=file.read()

data = data.replace('\n','')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
data= tokenizer.tokenize(data)

subj =[[] for i in range(len(data))]
verb =[[] for i in range(len(data))]
obj  =[[] for i in range(len(data))]
tell_time =  [[] for i in range(len(data))]

for i in range(len(data)):

    #removing stopwords
    data[i] = [w for w in data[i].split() if w not in stop_words]

    #tagging the words
    sentence = data[i]
    word = " ".join(sentence)
    sentences = nltk.sent_tokenize(word)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)


    #finding subject, verb and object
    ts = tagged_sentences[0]
    j=0
    flag = 0
    match = 0
    while j< len(ts):
        if ts[j][0] in time:
            tell_time[i].append(ts[j][0])
        match = 0
        if ts[j][1] == 'NNP' or ts[j][1] == 'PRP' or ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN':
            subj[i].append(ts[j][0])
            j+=1
            flag = 1
            match = 1

        if j <len(ts) and flag == 1 and (ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG'):
                if ts[j][0] not in tell_time:
                    verb[i].append(ts[j][0])
                j+=1
                flag = 2
                
            
        if j<len(ts) and ts[j][1] =='NN' and flag != 0:
                obj[i].append(ts[j][0])
                j+=1
        
        if match == 0:
            j+=1

#repeat_question = 'y'
while(repeat_question == 'y' or repeat_question == 'Y'):
    choice = input('Enter \n 1 to know who \n 2 to know what \n 3 to know when \n 4 to know whats going\n 5 to exit \n')   
    if choice == '1':
        print('Subject List\n')        
        for k in subj:
            print (k)
    print()
    if choice == '4':
        print('Verb List')
        for k in verb:
                print (k)
    print()
    if choice == '2':
        print('Object List')
        for k in obj:
                print (k)
    if choice == '3':
        print('time List\n')        
        for k in tell_time:
                print (k)
    print()
    if choice == '5':
        exit()
    repeat_question = input('Want to know more(y/n)')
    
    
    
print()
print("=="*30)
file.close()

    
    






