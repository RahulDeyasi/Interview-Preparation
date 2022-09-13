def rearrange(str1):
    dic={}
    for x in str1:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]=dic[x]+1
    
