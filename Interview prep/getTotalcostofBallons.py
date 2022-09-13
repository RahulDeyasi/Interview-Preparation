t=int(input())
while(t>0):
    arr=list()
    sum1=0
    ballons1,ballons2=map(int,input().split())
    participants=int(input())
    for i in range(participants):
        a=list(map(int,input().split()))
        arr.append(a)
    for x in arr:
        arr1=x
        if arr1[0]==1:
            sum1+=ballons1
        if arr1[1]==1:
            sum1+=ballons2     
    print(sum1)
    t-=1
