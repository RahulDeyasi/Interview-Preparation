class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if(self.root==None):
            self.root=Node(data)
            return
        q=[]
        q.append(self.root)
        while(len(q)>0):
            temp=q.pop(0)
            if(temp.left==None):
                temp.left=Node(data)
                break
            else:
                q.append(temp.left)
            if(temp.right==None):
                temp.right=Node(data)
                break
            else:
                q.append(temp.right)
    def printAllDiagonal(self):
        dic=dict()
        d=0
        self.getDiagonal(self.root,d,dic)
        for i in sorted(dic):
            for j in dic[i]:
                print(j,end=" ")
            print()
    def getDiagonal(self,root,d,dic):
        if root is None:
            return
        try:
            dic[d].append(root.data)
        except:
            dic[d]=[root.data]
        if root.left!=None:
            self.getDiagonal(root.left,d+1,dic)
        if root.right!=None:
            self.getDiagonal(root.right,d,dic)

if __name__=="__main__":
    tree=BinaryTree()
    nodes=list(map(int,input().strip().split()))
    for x in nodes:
        tree.insert(x)
    tree.printAllDiagonal()
        


            
                
            
