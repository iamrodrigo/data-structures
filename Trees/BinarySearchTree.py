class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def createNode(self, value):
        return Node(value)

    def insert_recursive(self, value):
        self.root = self.insert_recursive_implementation(self.root, value)

    def insert_recursive_implementation(self, node, value):
        if not node:
            return self.createNode(value)
        elif node.value >= value:
            node.left = self.insert_recursive_implementation(node.left, value)
        else:
            node.right =  self.insert_recursive_implementation(node.right, value)
        return node

    def insert_iterative(self, value):
        node = self.root
        if node is None:
            self.root = self.createNode(value)
        else:
            while node is not None:
                if node.value >= value:
                    if node.left is None:
                        node.left = self.createNode(value)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = self.createNode(value)
                        break
                    else:
                        node = node.right


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


    def search_iterative(self, value):
        node = self.root

        while node is not None:
            if node.value == value:
                return node
            elif node.value > value:
                node = node.left
            else:
                node = node.right

    def insert_iterative_implementation(self, value):
        if not self.root:
            self.root = self.createNode(value)
            return

        while node is not None:
            if node.value >= value:
                node = node.left

    def preorder(self):
        self.preorder_implementation(self.root)
        print '\n'

    def preorder_implementation(self, node):
        if node is None:
            return

        print node.value,
        self.preorder_implementation(node.left)
        self.preorder_implementation(node.right)

    def inorder(self):
        self.inorder_implementation(self.root)
        print '\n'

    def inorder_implementation(self, node):
        if node is None:
            return

        self.inorder_implementation(node.left)
        print node.value,
        self.inorder_implementation(node.right)

    def postorder(self):
        self.postorder_implementation(self.root)
        print '\n'

    def postorder_implementation(self, node):
        if node is None:
            return

        self.postorder_implementation(node.left)
        self.postorder_implementation(node.right)
        print node.value,

    def depth(self):
        return self.depth_implementation(self.root)

    def depth_implementation(self, node):
        pass
        #reimplement

    def height(self):
        return self.height_implementation(self.root)

    def height_implementation(self, node):
        if node is None:
            return -1

        return max(self.height_implementation(node.left), self.height_implementation(node.right)) + 1


    def breadthFirst(self):
        nodes = [self.root]

        while len(nodes):
            node = nodes.pop(0)
            print node.value

            if node.left is not None:
                nodes.append(node.left)

            if node.right is not None:
                nodes.append(node.right)

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
            tempNode = node
            if not node.left and not node.right:
                node = None
            elif not node.right:
                node = node.left
            elif not node.left:
                node = node.right
            else:
                parentNode = node
                tempNode = node.left
                while tempNode and tempNode.right:
                    parentNode = tempNode
                    tempNode = tempNode.right

                parentNode.right = None
                tempNode.left = node.left
                tempNode.right = node.right
                node , tempNode = tempNode, node

            del tempNode

        return node

a = -1

bst = BST()
bst.insert_recursive(12)
bst.insert_recursive(5)
bst.insert_recursive(7)
bst.insert_recursive(3)
bst.insert_recursive(1)
bst.insert_recursive(9)
bst.insert_recursive(8)
bst.insert_recursive(11)
bst.insert_recursive(14)
bst.insert_recursive(13)
bst.insert_recursive(17)
bst.insert_recursive(20)
bst.insert_recursive(18)

while a != 0:
    print "Binary Search Tree"
    print "1. Insert (Recursive)"
    print "2. Insert (Iterative)"
    print "3. Search (Recursive)"
    print "4. Search (Iterative)"
    print "5. Preorder"
    print "6. Inorder"
    print "7. Postorder"
    print "8. Depth"
    print "9. Height"
    print "10. Breadth First"
    print "11. Delete node"
    print "12. Min"
    print "13. Max"
    print "0. Exit"
    a = input("Choose an option: ")

    if a == 1:
        bst.insert_recursive(input("Introduce value to append: "))
    if a == 2:
        bst.insert_iterative(input("Introduce value to append: "))
    if a == 3:
        print 'YES' if bst.search_recursive(input("Introduce value to search: ")) else 'NO'
    if a == 4:
        print 'YES' if bst.search_iterative(input("Introduce value to search: ")) else 'NO'
    if a == 5:
        bst.preorder()
    if a == 6:
        bst.inorder()
    if a == 7:
        bst.postorder()
    if a == 8:
        print bst.depth()
    if a == 9:
        print bst.height()
    if a == 10:
        bst.breadthFirst()
    if a == 11:
        bst.delete(input("Introduce node to delete: "))


