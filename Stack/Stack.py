class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, node):
        node.next = self.head
        self.head = node

    def isEmpty(self):
        return False if self.head else True

    def pop(self):
        node = self.head

        if self.isEmpty():
            return node

        self.head = node.next
        return node.value

    def top(self):
        return self.head if self.isEmpty() else self.head.value

    def printNodes(self):
        list = []
        element = self.head
        while element:
            list.append(element.value)
            element = element.next

        return list

a = -1

s = Stack()

while a != 0:
    print "Stack"
    print "1. Push"
    print "2. Pop"
    print "3. Top"
    print "4. is empty"
    print "5. Print Stack"
    print "0. Exit"
    a = input("Choose an option: ")

    if a == 1:
        s.push(Node(input("Introduce value to push: ")))
    elif a == 2:
        print "The value popped is " + str(s.pop())
    elif a == 3:
        print "The value at the top is " + str(s.top())
    elif a == 4:
        print s.isEmpty()
    print s.printNodes()

