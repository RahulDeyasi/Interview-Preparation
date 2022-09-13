def pairSum(arr,k):
    if len(arr)<2:
        return
    seen=set()
    output=set()
    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num),max(target,num)))
    print(','.join(map(str,output)))
if __name__=="__main__":
    arr=list(map(int,input().strip().split()))
    k=int(input())
    pairSum(arr,k)
