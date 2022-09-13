def countingSort(arr,exp):
    n=len(arr)
    output=[0]*n
    count=[0]*10
    for i in range(0,n,1):
        index=int(arr[i]/exp)
        count[(index)%10]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=int(arr[i]/exp)
        output[count[(index%10)]-1]=arr[i]
        count[(index)%10]-=1
        i-=1
    for i in range(0,n):
        arr[i]=output[i]
    
def radixSort(arr):
    n=len(arr)
    max1=max(arr)
    exp=1
    while int(max1/exp)>0:
        countingSort(arr,exp)
        exp*=10
arr=list(map(int,input().strip().split()))
radixSort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
