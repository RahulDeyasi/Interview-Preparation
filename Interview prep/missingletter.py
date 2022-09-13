from collections import OrderedDict
def missingChar(s1,s2):
    d1=OrderedDict()
    d2=OrderedDict()
    for i in s1:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
    for j in s2:
        if j not in d2:
            d2[j]=1
        else:
            d2[j]+=1
    for i in d1:
        if i not in d2:
            print(i,end='')
        else:
            n=d1[i]-d2[i]
            for j in range(n):
                print(i,end='')    
str1=input().split()
missingChar(str1[0],str1[1])
