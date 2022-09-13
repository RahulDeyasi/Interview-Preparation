class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
            return
        q=[]
        q.append(self.root)
        while len(q)>0:
            temp=q.pop(0)
            if temp.left==None:
                temp.left=Node(data)
                break
            else:
                q.append(temp.left)
            if temp.right==None:
                temp.right=Node(data)
                break
            else:
                q.append(temp.right)
     
    def maxHorizontalSum(self,root):
        if root==None:
            return
        result=0
        q=[]
        q.append(root)
        while len(q)>0:
            count=len(q)
            sum1=0
            while count:
                temp=q.pop(0)
                sum1+=temp.data
                if temp.left!=None:
                    q.append(temp.left)
                if temp.right!=None:
                    q.append(temp.right)
                count-=1
            result=max(result,sum1)
        return result
    def maxVerticalSum(self,root):
        dic=dict()
        hd=0
        result=0
        self.getVerticalDistance(root,hd,dic)
        for i in sorted(dic):
            sum1=0
            for j in dic[i]:
                '''print(j,end=" ")'''
                sum1+=j
            result=max(result,sum1)
        return result
    def getVerticalDistance(self,root,hd,dic):
        if root is None:
            return
        try:
            dic[hd].append(root.data)
        except:
            dic[hd]=[root.data]
        if root.left!=None:
            self.getVerticalDistance(root.left,hd-1,dic)
        if root.right!=None:
            self.getVerticalDistance(root.right,hd+1,dic)
                      
if __name__=='__main__':
    Tree=BinaryTree()
    nodes=list(map(int,input().strip().split()))
    for x in nodes:
        Tree.insert(x)
    result1=Tree.maxHorizontalSum(Tree.root)
    result2=Tree.maxVerticalSum(Tree.root)
    print(result1+result2)
    
