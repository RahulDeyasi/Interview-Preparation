def evalutionPostfix(exp):
    stack=[]
    for i in range(len(exp)):
        c=exp[i]
        if ord(c)>=48 and ord(c)<=57:
            stack.append(c)
        else:
            val1=int(stack.pop())
            val2=int(stack.pop())
            if c=='+':
                stack.append(str(val2+val1))
                
            if c=='-':
                stack.append(str(val2-val1))
                
            if c=='*':
                stack.append(str(val2*val1))
                
            if c=='/':
                stack.append(str(val2/val1))
                
                
    return stack.pop()
if __name__=="__main__":
    exp=input()
    print(evalutionPostfix(exp))
    
            
 
            
