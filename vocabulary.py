def chartonumber(char):
    return ord(char)-48
def stringtonumber(str):
    n=len(str)-1
    sum=0
    mul=1
    while n>=0:
        sum+=(mul*chartonumber(str[n]))
        n-=1
        mul*=10
    return sum

def sent_tokenize(corpus):
    sentences=[]
    sent=""
    for i in range(len(corpus)):
        if corpus[i]=='.':
            if len(sent)!=0:
                sentences.append(sent)
            sent=""
        else:
            sent+=corpus[i]
    if len(sent)!=0:
        sentences.append(sent)
    return sentences
def word_tokenize(sentence):
    words=[]
    word=""
    for i in range(len(sentence)):
        if sentence[i]==' ':
            if len(word)!=0:
                words.append(word)
            word=""
        else:
            word+=sentence[i]
    if len(word)!=0:
        words.append(word)   
    return words
def are_same(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        if x[i]!=y[i]:
            return False
    return True
    
def vocabulary(words):
    voc=[]
    for i in range(len(words)):
        not_found=True
        for j in range(i):
            if are_same(words[i],words[j]):
                not_found=False
                break
        if not_found:
            voc.append(words[i])
    return voc
corpus="salman is a very good boy.he is hard working.salman wants to become successful in this and hereafter life."
sentences=sent_tokenize(corpus)
words_list=[]
for sent in sentences:
    words=word_tokenize(sent)
    for word in words:
        words_list.append(word)

unique_words=vocabulary(words_list)
