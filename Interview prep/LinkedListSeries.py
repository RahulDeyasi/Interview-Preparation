class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head==None:
            self.head=new_node
            return
        curr_node=self.head
        while curr_node.next is not None:
            curr_node=curr_node.next
        curr_node.next=new_node
    def Print(self):
        if self.head==None:
            print(' ')
            return
        curr_node=self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next

if __name__=='__main__':
    lList=LinkedList()
    nodes=list(map(int,input().strip().split()))
    rear=self.head
    front=self.head
    for x in nodes:
        lList.append(x)
        rear=rear.next
        
    
    
            
