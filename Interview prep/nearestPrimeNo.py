import math
def isPrime(x):
    flag=True
    for i in range(2,x):
        if x%i==0:
            flag=False
    return flag
if __name__=="__main__":
    x=int(input())
    prime1=1
    prime2=1
    for i in range(1,x,1):
        if isPrime(x-i):
            prime1=i
            
    for j in range(1,x,1):
        if isPrime(x+j):
            prime2=j
        
    if abs(prime1-x)<abs(prime2-x):
        print(prime1)
    else:
        print(prime2)
