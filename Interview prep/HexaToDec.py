str1=input()
result=0
for i in range(0,len(str1)):
    rem=0
    if ord(str1[-i-1])>=48 and ord(str1[-i-1])<=58:
        k=ord(str1[-i-1])-48
        rem=k%16
        result=result+pow(16,i)*rem
    if ord(str1[-i-1])>=65 and ord(str1[-i-1])<=70:
        z=ord(str1[-i-1])-55
        rem=z%16
        result=result+pow(16,i)*rem
print(result)
        
