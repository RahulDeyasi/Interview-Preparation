class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,new_data):
        if(self.root==None):
            self.root=Node(new_data)
            return
        q=[]
        q.append(self.root)
        while(len(q)>0):
            temp=q.pop(0)
            if(temp.left==None):
                temp.left=Node(new_data)
                break
            else:
                q.append(temp.left)
            if(temp.right==None):
                temp.right=Node(new_data)
                break
            else:
                q.append(temp.right)
    def getHorizontalOrderTree(self):
        output=[]
        q=[]
        q.append(self.root)
        while(len(q)>0):
            temp=q.pop(0)
            output.append(temp.data)
            if(temp.left!=None):
                q.append(temp.left)
            if(temp.right!=None):
                q.append(temp.right)
        return output        
    def TopView(self,root):
        dic=dict()
        hd=0
        horizontalTree=self.getHorizontalOrderTree()
        self.getHorizontalDistance(root,hd,dic)
        for i in sorted(dic):
            if len(dic[i])==1:
                n=dic[i]
                print(n[0],end=" ")
            else:
                minIndex=horizontalTree[len(horizontalTree)-1]
                for j in dic[i]:
                    for k in range(0,len(horizontalTree)):
                        if(j==horizontalTree[k]):
                            minIndex=min(minIndex,k)
                print(horizontalTree[minIndex],end=" ")
                                          
    def getHorizontalDistance(self,root,hd,dic):
        if root is None:
            return
        try:
            dic[hd].append(root.data)
        except:
            dic[hd]=[root.data]
        if root.left!=None:
            self.getHorizontalDistance(root.left,hd-1,dic)
        if root.right!=None:
            self.getHorizontalDistance(root.right,hd+1,dic)

if __name__=="__main__":
    tree=BinaryTree()
    nodes=list(map(int,input().strip().split()))
    for x in nodes:
        tree.insert(x)
    tree.TopView(tree.root)
        
    
