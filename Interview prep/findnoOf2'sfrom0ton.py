def numberOf2s(n):
    count=0
    for i in range(1,n+1,1):
        i=str(i)
        a=list(i)
        for j in range(len(a)):
            if a[j]=='2':
                count+=1
        del a
    print(count)
if __name__=="__main__":
    N=int(input())
    numberOf2s(N)
