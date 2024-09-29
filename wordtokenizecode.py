def word_tokenize(sentence):
    words=[]
    word=""
    for i in range(len(sentence)):
        if sentence[i]==' ':
            if len(word)!=0:
                words.append(word)
            word=""
        else:
            if sentence[i].isalpha() or sentence[i].isdigit():
                word+=sentence[i]
    
    if len(word)!=0:
        words.append(word)
    return words
text=input("enter sentence:")
words=word_tokenize(text)

print(words)
