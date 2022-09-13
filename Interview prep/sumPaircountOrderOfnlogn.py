def countPair(arr,k): 
    arr=sorted(arr)
    count=0
    left=0
    right=len(arr)-1
    while left<right:
        currentSum=arr[left]+arr[right]
        if currentSum==k:
            count+=1
            left+=1
        elif currentSum<k:
            left+=1
        else:
            right-=1     
    return count

if __name__=="__main__":
    arr=list(map(int,input().strip().split()))
    arr.sort()
    k=int(input())
    print(countPair(arr,k))
