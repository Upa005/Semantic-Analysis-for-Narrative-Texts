#answer wh questions in a paragraph
import nltk
import nltk.data
from nltk.tokenize import word_tokenize
from prettytable import PrettyTable
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
combine_list = []
for i in range(len(data)):

    #removing stopwords
    #data[i] = [w for w in data[i].split() if w not in stop_words]

    #tagging the words
    sentence = data[i].split()
    word = " ".join(sentence)
    sentences = nltk.sent_tokenize(word)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    #print(tagged_sentences)
    #print('\n')

    #finding subject, verb and object
    ts = tagged_sentences[0]
    j=0
    flag = 0
    match = 0
    while j< len(ts):
        if ts[j][0] in time:
            tell_time[i].append(ts[j][0])
        match = 0
        if flag == 0 and (ts[j][1] == 'NNP' or ts[j][1] == 'PRP'or ts[j][1] == 'PRP$' or ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN'):
            subj[i].append(ts[j][0])
            combine_list.append(ts[j][0])
            j+=1
            flag = 1
            match = 1

        if j <len(ts) and flag == 1 and (ts[j][1] =='VBZ' or ts[j][1] =='VB' or ts[j][1] =='VBD' or ts[j][1] =='VBN' or ts[j][1] =='VBP' or ts[j][1] =='VBG'):
                if ts[j][0] not in tell_time:
                    verb[i].append(ts[j][0])
                    combine_list.append(ts[j][0])
                j+=1
                
                
            
        if j<len(ts) and flag != 0 and (ts[j][1] == 'NNP' or ts[j][1] =='NNS' or ts[j][1] =='NNPS' or ts[j][1] == 'NN'):
                obj[i].append(ts[j][0])
                combine_list.append(ts[j][0])
                j+=1
        
        if match == 0:
            j+=1

#new_days = open(new_path,'w')
write_file = open('mytestfile.txt','w') 
t1 = PrettyTable(['Subj','Verb','Obj'])


for i in range(len(data)):
    t1.add_row([subj[i],verb[i],obj[i]])
    #combine_list.append(subj[i])
    #combine_list.append(verb[i])
    #combine_list.append(obj[i])

print(combine_list) 
write_file.write(str(t1))
print(t1)
print("=="*30)
file.close()
write_file.close() 
    






