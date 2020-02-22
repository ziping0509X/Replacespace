
#好未来2017秋招测试
#输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
# 例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”

def delete_same(s1,s2):
    s1,s2=list(s1),list(s2)
    list_1=[]

    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j]==s2[i]:
                list_1.append(s1[j])

    for l in range(len(list_1)):
        s1.remove(list_1[l])

    s1 = [str(i) for i in s1]
    s1 = ''.join(s1)
    return s1

def delete_same1(s1,s2):
    s1, s2 = list(s1), list(s2)
    s1_1=s1[:]
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j] == s2[i]:
                s1_1.remove(s2[i])

    s1_1 = [str(i) for i in s1_1]
    s1_1 = ''.join(s1_1)
    return s1_1

s1="They are students."
s2="aeiou"

s1=delete_same1(s1,s2)
print(s1)


def delete_same1(s1,s2):
    s1, s2 = list(s1), list(s2)
    s1_1=s1[:]
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j] == s2[i]:
                s1_1.remove(s2[i])

    s1_1 = [str(i) for i in s1_1]
    s1_1 = ''.join(s1_1)
    return s1_1

s1=raw_input()
s2=raw_input()
s1=delete_same1(s1,s2)
print(s1)

#调试成功！
#但remove函数的使用时python特有的。