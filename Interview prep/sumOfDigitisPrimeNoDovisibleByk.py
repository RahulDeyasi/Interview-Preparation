import math
def solve(a,b,k):
    arr=[0]*(b+1)
    arr[0]=arr[1]=False
    arr1=list()
    count=0
    for i in range(2,int(math.sqrt(b))+1):
        for j in range(i*i,b+1,i):
            arr[j]=False
    for i in range(2,b+1):
        if arr[i]==True:
            print(i,end=" ")
    '''for i in range(a,b+1,1):
        n=str(i)
        sum=0
        for j in range(0,len(n)):
            sum+=int(n[j])
        if i%k==0:
            if sum in arr1:
                count+=1
    return count'''
if __name__=="__main__":
    a,b,k=map(int,input().split())
    solve(a,b,k)
        
