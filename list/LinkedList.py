class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, node = None):
        self.head = node

    def append(self, node):
        element = self.head
        if element is None:
            self.head = node
        else:
            while element.next != None:
                element = element.next
            element.next = node

    def getPositionOfValue(self, value):
        element = self.head
        position = 0
        while element:
            position += 1
            if element.value == value:
                return "The value " + str(value) +" is in the position " + str(position)
            element = element.next
        return "The value was not found"

    def getValueOfPosition(self, position):
        element = self.head
        tempPosition = 0
        while element:
            tempPosition += 1
            if tempPosition == position:
                return "The position " + str(position) + " has the value " + str(element.value) + " on the list"
            element = element.next
        return "The position doesn't exist in the list"



    def insert(self, node, position):
        currentPosition = 0
        if position == 1:
            node.next = self.head
            self.head = node
            return
        else:
            element = self.head
            while element and position > currentPosition:
                currentPosition += 1
                if currentPosition + 1 == position:
                    tempNode = element.next
                    element.next = node
                    node.next = tempNode
                    print "Node Inserted"
                    return
                element = element.next
        print "The list is has a length of " + str(currentPosition) + ", so the element was not inserted"


    def deleteValue(self, value):
        node = self.head
        if node:
            if node.value == value:
                self.head = node.next
                del node
            else:
                while node:
                    next = node.next
                    if next and next.value == value:
                        node.next = next.next
                        del next
                        break
                    else:
                        node = next

    def deleteNode(self, n):
        node = self.head
        if n == 1:
            self.head = self.head.next
            del node
        else:
            counter = 1
            while node and counter < n:
                if counter + 1 == n:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    break
                counter += 1
                node = node.next

    def printNodes(self):
        list = []
        element = self.head
        while element:
            list.append(element.value)
            element = element.next

        return list

    def reverseListLoop(self):
        p1 = self.head
        p = None
        while p1:
            p2 = p1.next
            p1.next = p
            p = p1
            p1 = p2

        self.head = p

    def reverseListRecursion(self, n):
        if n.next is None:
            return n

        head = self.reverseListRecursion(n.next)

        n.next.next = n
        n.next = None
        return head

    def sizeOfLinkedList(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next

        print "Linked list has " + str(count) + " node(s)"

    def valueNFromTheEnd(self, n):
        p1 = p2 = self.head
        for i in xrange(n):
            if p2 is not None:
                p2 = p2.next
            else:
                print "N is invalid"
                return

        if p2 == None:
            print "The value of the " + str(n) + " node is " + str(p1.value)
            return

        while p2 != None:
            p1 = p1.next
            p2 = p2.next

        print "The value of the " + str(n) + " node is " + str(p1.value)



a = -1

ll = LinkedList()

while a != 0:
    print "Linked List"
    print "1. Append"
    print "2. Get Position Of Value"
    print "3. Get Value Of Position"
    print "4. Insert"
    print "5. Delete (Value)"
    print "6. Delete (Node)"
    print "7. Reverse list (loop)"
    print "8. Reverse list (recursion)"
    print "9. Print LinkedList"
    print "10. Size of LinkedList"
    print "11. Value n from the end"
    print "0. Exit"
    a = input("Choose an option: ")

    if a == 1:
        ll.append(Node(input("Introduce value to append: ")))
    elif a == 2:
        print ll.getPositionOfValue(input("Introduce value to search it's position: "))
    elif a == 3:
        print ll.getValueOfPosition(input("Introduce position to search it's value: "))
    elif a == 4:
        print ll.insert(Node(input("Introduce value to insert: ")), input("Introduce which position you want to insert the node: "))
    elif a == 5:
        ll.deleteValue(input("Introduce value of the node to be deleted: "))
    elif a == 6:
        ll.deleteNode(input("Introduce node to delete: "))
    elif a == 7:
        ll.reverseListLoop()
    elif a == 8:
        ll.head = ll.reverseListRecursion(ll.head)
    elif a == 10:
        ll.sizeOfLinkedList()
    elif a == 11:
        ll.valueNFromTheEnd(input("Introduce value of n (from the end): "))


    print ll.printNodes()

