def Merge(Left,Right,arr):
    nL=len(Left)
    nR=len(Right)
    i=j=k=0
    while i<nL and j<nR:
        if Left[i]<=Right[j]:
            arr[k]=Left[i]
            i+=1
        else:
            arr[k]=Right[j]
            j+=1
        k+=1
    while i<nL:
        arr[k]=Left[i]
        i+=1
        k+=1
    while j<nR:
        arr[k]=Right[j]
        j+=1
        k+=1
        
def MergeSort(arr):
    n=len(arr)
    if n<2:
        return
    mid=int(n/2)
    Left=[0]*mid
    Right=[0]*(n-mid)
    for i in range(0,mid):
        Left[i]=arr[i]
    for j in range(mid,n):
        Right[j-mid]=arr[j]
    MergeSort(Left)
    MergeSort(Right)
    Merge(Left,Right,arr)

arr=list(map(int,input().strip().split()))
MergeSort(arr)
print(arr)
    
       
