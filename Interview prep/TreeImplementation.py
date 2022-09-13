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
        else:
            self._insert(data,self.root)
    def _insert(self,data,curr_node):
        if curr_node.data<data:
            if curr_node.right==None:
                curr_node.right=Node(data)
            else:
                self._insert(data,curr_node.right)
        else:
            if curr_node.left==None:
                curr_node.left=Node(data)
            else:
                self._insert(data,curr_node.left)
                
    def printPreorder(self):
        if self.root==None:
            return
        else:
            self._printPreorder(self.root)
            
    def _printPreorder(self,curr_node):
        print(curr_node.data,end=" ")
        if curr_node.left is not None:
            self._printPreorder(curr_node.left)
        if curr_node.right is not None:
            self._printPreorder(curr_node.right)
            
    def printInorder(self):
        if self.root==None:
            return
        else:
            self._printInorder(self.root)
            
    def _printInorder(self,curr_node):
        if curr_node.left != None:
            self._printInorder(curr_node.left)
        print(curr_node.data,end=" ")
        if curr_node.right != None:
            self._printInorder(curr_node.right)
            
    def printPostorder(self):
        if self.root==None:
            return
        else:
            self._printPostorder(self.root)
            
    def _printPostorder(self,curr_node):
        if curr_node.left != None:
            self._printPostorder(curr_node.left)
        if curr_node.right != None:
            self._printPostorder(curr_node.right)
        print(curr_node.data,end=" ")
    def printLevelorder(self,root):
        q=[]
        if self.root is None:
            return
        q.append(root)
        while(len(q)>0):
            print(q[0].data,end=" ")
            node=q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)             
if __name__=='__main__':
    Tree=BinaryTree()
    nodes=list(map(int,input().strip().split()))
    for x in nodes:
        Tree.insert(x)
    '''Tree.printPreorder()
    print()
    Tree.printInorder()
    print()
    Tree.printPostorder()
    print()'''
    Tree.printLevelorder(Tree.root)
            
            
