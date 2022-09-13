def countSort(arr,k):
    n=len(arr)
    output=[0]*n
    count=[0]*k
    for i in range(0,n,1):
        count[arr[i]]+=1
    for i in range(1,k,1):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        output[count[arr[i]-1]]=arr[i]
        count[arr[i]]-=1
    for i in range(0,n,1):
        arr[i]=output[i]
    return arr
arr=list(map(int,input().strip().split()))
k=int(input())
print(countSort(arr,k))

        
