from collections import defaultdict
d=defaultdict(int)
str1=input()
for x in str1:
    d[x]+=1
for i in d:
    print(i,"-->",d[i])


'''str2=input().lower()
dict1={}
for i in str2:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
for x in dict1:
    print(x,"-->",dict1[x])'''
