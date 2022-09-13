def partition(arr,start,end):
    pivot=arr[end]
    pindex=start
    for i in range(start,end):
        if arr[i]<=pivot:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[pindex],arr[end]=arr[end],arr[pindex]
    return pindex
   
def quickSort(arr,start,end):
    if start<end:
        pindex=partition(arr,start,end)
        quickSort(arr,start,pindex-1)
        quickSort(arr,pindex+1,end)

arr=list(map(int,input().strip().split()))
quickSort(arr,0,len(arr)-1)
print(arr)

