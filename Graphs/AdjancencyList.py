class AdancencyList(object):
    def __init__(self):
        self.vertexList = []
        self.edgeMatrix = []
        self.numberOfVertex = 0

    def createVertex(self, value):
        self.vertexList.append(value)
        self.edgeMatrix.append([])

    def connectVertices(self, vertexA, vertexB):
        vertexAIndex = self.vertexList.index(vertexA)
        vertexBIndex = self.vertexList.index(vertexB)

        self.edgeMatrix[vertexAIndex].append(vertexBIndex)
        self.edgeMatrix[vertexBIndex].append(vertexAIndex)

    def findAdjacentVertex(self, vertex):
        vertexIndex = self.vertexList.index(vertex)
        for v in self.edgeMatrix[vertexIndex]:
            print "Vertex {} is connected with vertex {}".format(vertex, self.vertexList[v])

    def areVertexConnected(self, vertexA, vertexB):
        vertexAIndex = self.vertexList.index(vertexA)
        vertexBIndex = self.vertexList.index(vertexB)

        for v in self.edgeMatrix[vertexAIndex]:
            if v == vertexBIndex:
                return True

        return False

a = -1

g = AdancencyList()
g.createVertex('A')
g.createVertex('B')
g.createVertex('C')
g.createVertex('D')
g.createVertex('E')
g.createVertex('F')
g.createVertex('G')
g.createVertex('H')
g.connectVertices('A', 'B')
g.connectVertices('A', 'C')
g.connectVertices('A', 'D')
g.connectVertices('C', 'G')
g.connectVertices('G', 'H')
g.connectVertices('H', 'D')
g.connectVertices('H', 'E')
g.connectVertices('H', 'F')
g.connectVertices('F', 'B')
g.connectVertices('B', 'E')

g.findAdjacentVertex('A')
g.findAdjacentVertex('B')
g.findAdjacentVertex('C')
g.findAdjacentVertex('D')
g.findAdjacentVertex('E')
g.findAdjacentVertex('F')
g.findAdjacentVertex('G')
g.findAdjacentVertex('H')

print g.areVertexConnected('A', 'E')
print g.areVertexConnected('A', 'B')
print g.areVertexConnected('C', 'G')
print g.areVertexConnected('F', 'E')
print g.areVertexConnected('F', 'A')


while a != -1:
    print "Adjacency List (Graphs)"
    a = input("Choose an option: ")

    if a == 1:
        pass



