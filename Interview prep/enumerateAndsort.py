dic={-3:[6,8,2],-1:[3,5,1],0:[2,9,4],-2:[2,5,1],1:[3,4,1],2:[4,7,1]}
'''for index,values in enumerate(sorted(dic)):
    for i in dic[values]:
        print(i,end=" ")
    print()'''
for i in sorted(dic):
    for j in dic[i]:
        print(j,end=" ")
    
        
