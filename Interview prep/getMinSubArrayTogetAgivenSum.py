def minSubArrayTogetAgivenSum(arr,k):
    start=0
    end=len(arr)-1
    m=list()
    while(start<end):
        getMinSubArray(arr,start,end,k,m)
        start+=1
    result=min(m)
    print(result)
def getMinSubArray(arr,start,end,k,m):
    sum=0
    for i in range(start,end+1,1):
        if sum<k:
            sum+=arr[i]
        if sum==k:
            m.append(i-start+1)
            break
        if sum>k:
            break
arr=list(map(int,input().strip().split()))
k=int(input())
minSubArrayTogetAgivenSum(arr,k)
