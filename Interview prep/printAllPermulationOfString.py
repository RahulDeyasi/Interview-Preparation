def toString(List):
    return ''.join(List)
def permutation(s,l,r):
    if l==r:
        print(toString(s))
    for i in range(l,r+1,1):
        s[l],s[i]=s[i],s[l]
        permutation(s,l+1,r)
        s[l],s[i]=s[i],s[l]
string="ABC"
n=len(string)
s=list(string)
permutation(s,0,n-1)
        
