class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def enqueue(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def isEmpty(self):
        return False if self.head else True

    def dequeue(self):
        node = self.head
        if node:
            self.head = self.head.next
        return self.head if not node else node.value


    def peek(self):
        return self.head if self.isEmpty() else self.head.value

    def printNodes(self):
        list = []
        element = self.head
        while element:
            list.append(element.value)
            element = element.next

        return list

a = -1

s = Queue()

while a != 0:
    print "Queue"
    print "1. Enqueue"
    print "2. Dequeue"
    print "3. Peek"
    print "4. Is empty"
    print "5. Print Queue"
    print "0. Exit"
    a = input("Choose an option: ")

    if a == 1:
        s.enqueue(Node(input("Introduce value to enqueue: ")))
    elif a == 2:
        print "The value dequeued is " + str(s.dequeue())
    elif a == 3:
        print "The value at the top is " + str(s.peek())
    elif a == 4:
        print s.isEmpty()
    print s.printNodes()

