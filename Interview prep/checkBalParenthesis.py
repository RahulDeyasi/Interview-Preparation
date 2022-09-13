def checkBalParenthesis(exp):
    if (len(exp)%2)!=0:
        return False
    opening=set('({[')
    match=set([('(',')'),('{','}'),('[',']')])
    stack=[]
    for ch in exp:
        if ch in opening:
            stack.append(ch)
        else:
            lastOpen=stack.pop()
            if (lastOpen,ch) not in match:
                return False
    return len(stack)==0

if __name__=="__main__":
    exp=input()
    print(checkBalParenthesis(exp))
