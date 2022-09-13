def solve(n,m):
    result=0
    while(n>=m):
        result+=int(n/m)
        n=int(n/m)+(n%m)
    return result
t=int(input())
while(t>0):
    n,m=map(int,input().split())
    print(solve(n,m))
    t-=1
