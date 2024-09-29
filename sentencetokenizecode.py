def sent_tokenize(corpus):
    sents=[]
    sent=""
    for i in range(len(corpus)):
        if corpus[i]=='.':
            if len(sent)!=0:
                sents.append(sent)
            sent=""
        else:
            if corpus[i].isalpha() or corpus[i].isdigit():
                sent+=corpus[i]
    
    if len(sent)!=0:
        sents.append(sent)        
    return sents
corpus=input("enter text:")
sentences=sent_tokenize(corpus)
print(sentences)
