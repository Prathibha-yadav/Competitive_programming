class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class LinkedList :
    def __init__(self):
        self.head = None
    def addElement(self, value):
        newNode = Node(value)
        if(self.head == None):
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
            
    def removeElement(self,value):
        cur = self.head
        prev = None
        found = False
        if value == self.head.data:
            self.head = self.head.next
            return True
        while cur.data != value and cur.next != None:
            prev = cur
            cur = cur.next
        if cur.data == value:
            found = True
            prev.next = cur.next
            return True
        else :
            return False
    def searchElement(self,value):
        cur = self.head
        if value == self.head.data:
            self.head = self.head.next
        while cur.data != value and cur.next != None:
            cur = cur.next
        if cur.data == value:
            print("Value Found")
        else :
            print("Value Not Found")
            
    def printList(self):
        cur = self.head
        while cur.next != None:
            print(cur.data, end="->")
            cur = cur.next
        print(cur.data)

    def UpdateElement(self):
        cur = self.head
        while cur.next != None:
            print(cur.data, end="->")
            cur = cur.next
        print(cur.data)
    
lst = LinkedList()
lst.addElement(10)
lst.addElement(20)
lst.addElement(30)
lst.addElement(40)
lst.addElement(50)


lst.removeElement(30)
lst.removeElement(50)
lst.printList()
lst.searchElement(40)

