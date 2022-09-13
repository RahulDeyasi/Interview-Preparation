def prevPrimeNo(n):
    while True:
        n-=1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n


def nextPrimeNo(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n
if __name__=="__main__":
    x=int(input())
    Lprime=prevPrimeNo(x)
    Nprime=nextPrimeNo(x)
    if abs(Lprime-x)<abs(Nprime-x):
        print(Lprime)
    else:
        print(Nprime)
    
