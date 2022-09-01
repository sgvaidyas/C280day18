class Node:
    def __init__(self,ele=None):
        self.data = ele
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.cnt = 0

    def insertBegin(self,ele):
        temp = Node(ele) #declare the object of another class => aggregation
        temp.next = self.head
        self.head = temp
        self.cnt += 1

    def insertEnd(self,ele):
        temp = Node(ele) #declare the object of another class => aggregation
        if self.head == None:
            self.head = temp
        else:
            ptr = self.head
            while ptr.next!=None:
                ptr = ptr.next
            ptr.next=temp
            self.cnt += 1

    def insertPos(self,pos,ele):
        if pos==1:
            self.insertBegin(ele)
        elif pos == self.cnt+1:
            self.insertEnd(ele)
        else:
            temp = Node(ele)
            pp =cp = self.head
            for i in range(1,pos):
                pp = cp
                cp = cp.next
            pp.next = temp
            temp.next = cp
            self.cnt+=1

    def deleteBegin(self):
        if self.head is None:
            print("Cannot delete as list is empty")
        else:
            print("Deleting  = ",self.head.data)
            ptr = self.head
            self.head = self.head.next
            del ptr
            self.cnt -=1

    def deleteEnd(self):
        if self.head is None:
            print("Cannot delete as list is empty")
        else:
            pp = cp = self.head
            while cp.next is not None:
                pp = cp
                cp = cp.next
            #if we had ----------- pp.next = None  ----------here
            print("Deleting  = ",cp.data)
            #then -------------    if pp==cp:
            if self.head.next is None:
                self.head = None
            pp.next = None
            del cp
            self.cnt -=1

    def deletePos(self,pos):
        if pos==1:
            self.deleteBegin()
        elif pos == self.cnt:
            self.deleteEnd()
        else:
            pp =cp = self.head
            for i in range(1,pos):
                pp = cp
                cp = cp.next
            pp.next = cp.next
            print("delete = ", cp.data)
            del cp
            self.cnt-=1


    def display(self):
        if self.head is None:
            print("LIST EMPTY")
        else:
            print("LIST ELEMENTS  ----------- ")
            ptr = self.head
            while ptr!=None:
                print(ptr.data , end=" ---> ")
                ptr = ptr.next
            print("NONE")

ob = SLL()
while True:
    print("1 Insert Begin ")
    print("2 Insert End ")
    print("3 Insert Pos ")
    print("4 Delete Begin ")
    print("5 Delete End ")
    print("6 Delete Pos ")
    print("7 Display ")
    print("8 Exit ")
    ch = int(input("Enter the choice = "))
    if ch==1:
        ele = int(input("Enter the ele  = "))
        ob.insertBegin(ele)
    elif ch==2:
        ele = int(input("Enter the ele  = "))
        ob.insertEnd(ele)
    elif ch==3:
        pos = int(input("Enter the pos  = "))
        if pos>0 and pos<=ob.cnt+1:
            ele = int(input("Enter the ele  = "))
            ob.insertPos(pos,ele)
        else:
            print("Invalid pos ")
    elif ch==4:
        ob.deleteBegin()
    elif ch==5:
        ob.deleteEnd()
    elif ch==6:
        pos = int(input("Enter the pos  = "))
        if pos>0 and pos<=ob.cnt:
            ob.deletePos(pos)
        else:
            print("Invalid pos ")
    elif ch==7:
        ob.display()
    elif ch==8:
        break
    else:
        print("Invalid choice")
