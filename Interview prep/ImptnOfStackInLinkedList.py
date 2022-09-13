class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.Top=None
    def push(self,new_data):
        new_node=Node(new_data)
        if self.Top==None:
            self.Top=new_node
            return
        new_node.next=self.Top
        self.Top=new_node
    def pop(self):
        if self.Top==None:
            return
        self.Top=self.Top.next
    def Print(self):
        curr_node=self.Top
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
if __name__=='__main__':
    lList=LinkedList()
    nodes=list(map(int,input().strip().split()))
    for x in nodes:
        lList.push(x)
    lList.Print()
    lList.pop()
    lList.pop()
    print()
    lList.Print()
        
        
