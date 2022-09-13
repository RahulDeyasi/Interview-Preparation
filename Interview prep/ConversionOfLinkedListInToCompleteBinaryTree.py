class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Conversion:
    def __init__(self):
        self.head=None
        self.root=None
    def insert(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def ConvertList2Binary(self):
        q=[]
        if self.head is None:
            self.root=None
            return
        self.root=BinaryTreeNode(self.head.data)
        q.append(self.root)
        self.head=self.head.next
        while (self.head):
            parent=q.pop(0)
            leftChild=None
            rightChild=None
            leftChild=BinaryTreeNode(self.head.data)
            q.append(leftChild)
            self.head=self.head.next
            if self.head:
                rightChild=BinaryTreeNode(self.head.data)
                q.append(rightChild)
                self.head=self.head.next
            parent.left=leftChild
            parent.right=rightChild
    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)
con=Conversion()
List=list(map(int,input().strip().split()))         
for i in List:      
    con.insert(i)
'''con.Inorder(con.head)'''
con.ConvertList2Binary()
con.Inorder(con.root)
          

              


            
            
                
        
