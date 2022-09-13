def getMinTime(arr):
    sum=0
    arr.sort()
    for i in range(1,len(arr)):
        sum+=arr[i]
        if arr[i]!=arr[-1]:
            sum+=arr[0]
    return sum
arr=list(map(int,input().strip().split()))
print(getMinTime(arr))
