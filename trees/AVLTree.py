class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
        self.balanceFactor = 0

class AVL(object):
    def __init__(self):
        self.root = None

    def createNode(self, value):
        return Node(value)

    def rotateRight(self, node):
        left = node.left
        leftRightChild = left.right
        node.left = leftRightChild
        left.right = node

        self.retrace(node)
        self.retrace(left)

        return left

    def rotateLeft(self, node):
        right = node.right
        rightLeftChild = right.left
        node.right = rightLeftChild
        right.left = node

        self.retrace(node)
        self.retrace(right)

        return right

    def insert(self, value):
        self.root = self.insert_implementation(self.root, value)

    def insert_implementation(self, node, value):
        if not node:
            node = self.createNode(value)
        elif value > node.value:
            node.right = self.insert_implementation(node.right, value)
        else:
            node.left = self.insert_implementation(node.left, value)

        self.retrace(node)
        return self.balance(node)

    def balance(self, node):
        balance = self.heightOfChildren(node)

        if balance  > 1:
            # Right Right
            if self.heightOfChildren(node.left) >= 0:
                node = self.rotateRight(node)
            # Left Right
            else:
                node.left = self.rotateLeft(node.left)
                node = self.rotateRight(node)
        elif balance < -1:
            # Left Left
            if self.heightOfChildren(node.right) <= 0:
                node = self.rotateLeft(node)
            # Right Left
            else:
                node.right = self.rotateRight(node.right)
                node = self.rotateLeft(node)

        return node

    def height(self, node):
        return node.height if node else -1

    def retrace(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        node.balanceFactor = self.height(node.left)- self.height(node.right)

    def heightOfChildren(self, node):
        return self.height(node.left) - self.height(node.right)

    def search_recursive(self, value):
        return self.search_recursive_implementation(value, self.root)

    def search_recursive_implementation(self, value, node):
        if node is None:
            return node
        elif(node.value == value):
            return node
        elif(node.value > value):
            return self.search_recursive_implementation(value, node.left)
        else:
            return self.search_recursive_implementation(value, node.right)

    def breadthFirst(self):
        nodes = [self.root]

        while len(nodes):
            node = nodes.pop(0)
            print node.value,

            if node.left is not None:
                nodes.append(node.left)

            if node.right is not None:
                nodes.append(node.right)

        print "\n"

    def delete(self, value):
        self.root = self.delete_implementation(self.root, value)

    def delete_implementation(self, node, value):

        if not node:
            return node

        if node.value > value:
            node.left = self.delete_implementation(node.left, value)
        elif node.value < value:
            node.right = self.delete_implementation(node.right, value)
        else:
            if not node.left and not node.right:
                node = None
                return node
            elif not node.right:
                node = node.left
            elif not node.left:
                node = node.right
            else:
                tempNode = node.left

                while tempNode.right:
                    tempNode = tempNode.right

                node.value = tempNode.value
                node.left = self.delete_implementation(node.left, tempNode.value)

        self.retrace(node)
        return self.balance(node)

a = -1

avl = AVL()

# RR Insertion
avl.insert(10) #A
avl.breadthFirst()
avl.insert(20) #Ar
avl.breadthFirst()
avl.insert(5)  #B
avl.breadthFirst()
avl.insert(7)  #Br
avl.breadthFirst()
avl.insert(3)  #C
avl.breadthFirst()
avl.delete(20)
avl.breadthFirst()
#avl.insert(1)  #Cl, balance activated
#avl.breadthFirst()

#LR Insertion
#avl.insert(10) #A
#avl.breadthFirst()
#avl.insert(20) #Ar
#avl.breadthFirst()
#avl.insert(5)  #B
#avl.breadthFirst()
#avl.insert(7)  #C
#avl.breadthFirst()
#avl.insert(3)  #Bl
#avl.breadthFirst()
#avl.insert(8)  #Cr, balance activated
#avl.breadthFirst()

#LL Insertion
#avl.insert(10) #A
#avl.breadthFirst()
#avl.insert(5) #Al
#avl.breadthFirst()
#avl.insert(20) #B
#avl.breadthFirst()
#avl.insert(15) #Bl
#avl.breadthFirst()
#avl.insert(30) #C
#avl.breadthFirst()
#avl.insert(40) #Cr #balance activated
#avl.breadthFirst()

#RL Insertion
#avl.insert(10) #A
#avl.breadthFirst()
#avl.insert(5) #Al
#avl.breadthFirst()
#avl.insert(20) #B
#avl.breadthFirst()
#avl.insert(15) #C
#avl.breadthFirst()
#avl.insert(30) #Br
#avl.breadthFirst()
#avl.insert(12) #Cl #balance activated
#avl.breadthFirst()


while a != 0:
    print "Binary Search Tree"
    print "1. Insert (Recursive)"
    print "2. Insert (Iterative)"
    print "3. Search (Recursive)"
    #print "9. Height"
    print "5. Breadth First"
    print "6. Delete node"
    print "0. Exit"
    a = input("Choose an option: ")

    if a == 1:
        avl.insert(input("Introduce value to append: "))
    if a == 2:
        pass
        #avl.insert_iterative(input("Introduce value to append: "))
    if a == 3:
        print 'YES' if avl.search_recursive(input("Introduce value to search: ")) else 'NO'
    if a == 5:
        avl.breadthFirst()
    if a == 6:
        avl.delete(input("Introduce node to delete: "))


