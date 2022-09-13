def heapify(arr,n,i):
    largest=i
    l=(2*i)+1
    r=(2*i)+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def buildheap(arr):
    n=len(arr)
    startIdx=int(n/2)-1
    for i in range(startIdx,-1,-1):
        heapify(arr,n,i)
def heapSort(arr):
    n=len(arr)-1
    for i in range(n,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

arr=list(map(int,input().strip().split()))
buildheap(arr)
heapSort(arr)
print(arr)

    
    
