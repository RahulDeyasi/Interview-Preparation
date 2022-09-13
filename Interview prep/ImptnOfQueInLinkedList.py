class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.front=None
        self.rear=None
    def Enqueue(self,new_data):
        new_node=Node(new_data)
        if self.front==None and self.rear==None:
            self.front=self.rear=new_node
            return
        curr_node=self.rear
        curr_node.next=new_node
        self.rear=new_node
    def Dequeue(self):
        if self.front==None:
            return
        self.front=self.front.next
    def Print(self):
        if self.front==None:
            print(' ')
            return
        curr_node=self.front
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        
    
if __name__=='__main__':
    lList=LinkedList()
    nodes=list(map(int,input().strip().split()))
    for x in nodes:
        lList.Enqueue(x)
    lList.Dequeue()
    lList.Print()
