
#剑指第2题
#请实现一个函数，将一个字符串中的每个空格替换成“%20”。
#例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

def Replacespace(char,lenth):
    char=list(char)
    for i in range(lenth):
        if char[i] == " ":
            char[i]="%20"
    char=[str(i) for i in char]
    char=''.join(char)
    return str(char)

sentence=input()
sentence_1=Replacespace(sentence,len(sentence))
print(sentence)
print(sentence_1)

#调试成功！













