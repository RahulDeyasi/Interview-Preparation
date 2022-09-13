import math
def printPrimeNo(n):
    prime=[True]*(n+1)
    prime[0]=prime[1]=False
    for i in range(2,int(math.sqrt(n))):
        if prime[i]==True:
            for j in range(i*i,n+1,i):
                    prime[j]=False   
    return prime

if __name__=="__main__":
    n=int(input())
    prime1=printPrimeNo(n)
    for i in range(2,len(prime1)):
        if prime1[i]==True:
            print(i,end=" ")
         
        
