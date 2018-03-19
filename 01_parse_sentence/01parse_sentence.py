#answer wh questions in a single sentence
import nltk
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

repeat_flag = 'y'
while(repeat_flag == 'y' or repeat_flag == 'Y'):

    # input the sentence
    print()
    sentence = input('Enter the sentence: ')
    print("=="*30)
    print()

    #removing punctuations
    tokenizer = RegexpTokenizer(r'\w+')
    sentence = tokenizer.tokenize(sentence)
    print(sentence)
    #sentence = sentence.split()

    #removing stopwords
    #es = {'against', 'in', 'to', 'because', 'couldn', 'should', 'was', 'who', 'doesn', 'itself', 'has', 'below', 'were', 'each', 'before', 'while', 'from', 'hasn', 'hers', 'off', 'when', 'ma', 'both', 'which', 'his', 'here', 'can', 'over', 'further', 'not', 'these', 'now', 'shan', 'ourselves', 'no', 'whom', 'of', 'under', 'then', 'few', 'had', 'so', 'do', 'the', 'does', 'didn', 'their', 'if', 'mightn', 'how', 've', 'hadn', 'once', 'into', 'been', 'more', 'those', 'y', 'am', 'weren', 'too', 're', 'an', 'after', 'with', 'our', 's', 'at', 'why', 'only', 'your', 'again', 'wouldn', 'a', 'all', 'm', 'very', 'by', 'herself', 'having', 'and', 'is', 'as', 'some', 'needn', 'be', 'or', 'yourself', 'ours', 'yours', 'being', 'any', 'll', 'o', 'for', 'above', 'up', 'yourselves', 'ain', 'haven', 'down', 'doing', 'did', 'won', 'that', 'himself', 'between', 'same', 'she', 'such', 'this', 'but', 'most', 'own', 'don', 'than', 'during', 'themselves', 'nor', 'just', 'until', 'where', 'them', 'about', 'theirs', 'd', 'what', 'aren', 'shouldn', 'it', 'are', 't', 'i', 'my', 'on', 'there', 'wasn', 'will', 'mustn', 'myself', 'out', 'isn', 'have', 'its', 'through', 'other', 'we'}
    es = ['was','a','who','and','to','in','this','would','the','for','till']
    sentence_filter = [w for w in sentence if w not in es]
    if sentence_filter != sentence:
    #   print('Sentence after removing stopwords',sentence_filter)
    #    print()
        sentence = sentence_filter
    
    #tagging the words
    word = " ".join(sentence)
    sentences = nltk.sent_tokenize(word)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    print(tagged_sentences)
    print()

    #finding subject, verb and object
    ts = tagged_sentences[0]
    i=0
    flag = 0
    match = 0
    while i< len(ts):
        match = 0
        if ts[i][1] == 'NNP' or ts[i][1] == 'PRP' or ts[i][1] =='NNS' or ts[i][1] =='NNPS' or ts[i][1] == 'NN':
            print('Subject: \t' ,(ts[i][0]))
            i+=1
            flag = 1
            match = 1

        if i <len(ts) and flag == 1 and (ts[i][1] =='VBZ' or ts[i][1] =='VB' or ts[i][1] =='VBD' or ts[i][1] =='VBN' or ts[i][1] =='VBP' or ts[i][1] =='VBG'):
                print ('Verb:    \t' ,ts[i][0])
                i+=1
                flag = 2

            
        if i<len(ts) and ts[i][1] =='NN' and flag != 0:
                print ('Object: \t',ts[i][0])
                i+=1
        
        if match == 0:
            i+=1

    print()
    print("=="*30)
    repeat_flag =input('You want to check again? (y/n)')









