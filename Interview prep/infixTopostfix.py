def prec(ch):
    if ch=='+' or ch=='-':
        return 1
    if ch=='*' or ch=='/':
        return 2
    if ch=='^':
        return 3
    else:
        return -1
        
def infixTopostfix(exp):
    postfixExp=""
    stack=[]
    stack.append('(')
    for i in exp:
        if ord(i)>=48 and ord(i)<=57:
            postfixExp+=i
        elif i=='(':
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!='(':
                postfixExp+=stack.pop()
            stack.pop()
        else:
            while stack and prec[i]<=prec[stack[-1]]:
                postfixExp+=stack.pop()
            stack.append(i)
    return postfixExp
if __name__=="__main__":
    exp=input()
    exp=exp+')'
    print(infixTopostfix(exp))
