def Addition(str1):
    temp=''
    sum1=0
    for i in range(len(str1)):
        if(str1[i].isdigit()):
            temp+=str1[i]
        elif(len(temp)!=0):
            sum1=sum1+int(temp)
            temp=''
        else:
            continue
        if(i==len(str1)-1):
            sum1=sum1+int(temp)
            temp=''
    return sum1
str1=input()
print(Addition(str1))
            
