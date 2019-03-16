class UnionFind(object):
    def __init__(self, elements = 10):
        self.elements = [i for i in xrange(elements)]
        #self.elements = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9, 10]
        self.size = [1] * elements

    def root(self, a):
        root = self.elements[a]
        while root != self.elements[root]:
            root = self.elements[root]

        while a != root:
            parent = self.elements[a]
            self.elements[a] = root
            a = parent

        return root

    def union(self, a, b):
        rootA = self.root(a)
        rootB = self.root(b)

        if rootA == rootB:
            return

        if self.size[rootA] >= self.size[rootB]:
            self.elements[rootB] = self.elements[rootA]
            self.size[rootA] += self.size[rootB]
            self.size[rootB] = 0
        else:
            self.elements[rootA] = self.elements[rootB]
            self.size[rootB] += self.size[rootA]
            self.size[rootA] = 0

    def find(self, a, b):
        return self.root(a) == self.root(b)


c = UnionFind(12)
#print c.find(0, 11)
#print c.find(0, 11)
c.union(4, 9)
c.union(1, 0)
c.union(5, 6)
c.union(5, 10)
c.union(4, 3)
c.union(3, 2)
c.union(7, 1)
c.union(4, 5)
c.union(5, 10)
c.union(11, 8)
c.union(11, 1)
c.union(11, 10)
c.find(8, 6)


