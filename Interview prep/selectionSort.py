def selectionSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        minVal_in=i
        for j in range(i+1,n):
            if arr[minVal_in]>arr[j]:
                minVal_in=j
        arr[i], arr[minVal_in] = arr[minVal_in], arr[i]
    return arr
if __name__=="__main__":
    arr=list(map(int,input().strip().split()))
    print(selectionSort(arr))
                
'''order of n**2          
