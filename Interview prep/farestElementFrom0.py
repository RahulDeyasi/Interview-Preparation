def findFarestElement(arr,n):
    index=0
    far=0
    for i in range(n+1):
        if arr[i]==0:
            index=i
            break
    Rfar=n-index
    Lfar=index
    if Rfar==Lfar:
        if arr[0]>=arr[n]:
            far=n
        else:
            far=0
    elif Rfar>Lfar:
        far=n
    else:
        far=0     
    print(arr[far])
if __name__=="__main__":
    arr=list(map(int,input().split()))
    findFarestElement(arr,len(arr)-1)
    
    
