def getCount(arr,p,q):
    count=0
    for i in range(len(arr)):
        sum=0
        k=0
        for j in range(i,len(arr)):
            if(sum<q):
                sum+=arr[j]
                k+=1
            if(sum==q and k>p):
                count+=1
            if(sum>q):
                break
    return count
n,p,q=map(int,input().strip().split())
arr=list(map(int,input().strip().split()))
print(getCount(arr,p,q))
