class VertexList(object):
    def __init__(self):
        self.vertexList = []
        self.edgeList = []
        self.numberOfVertex = 0

    def createVertex(self, value):
        self.vertexList.append(value)

    def connectVertices(self, vertexA, vertexB):
        self.edgeList.append((self.vertexList.index(vertexA), self.vertexList.index(vertexB)))

    def findAdjacentVertex(self, vertex):
        vertexIndex = self.vertexList.index(vertex)
        for v in self.edgeList:
            if v[0] == vertexIndex:
                print "Vertex {} is connected with vertex {}".format(vertex, self.vertexList[v[1]])
            elif v[1] == vertexIndex:
                print "Vertex {} is connected with vertex {}".format(vertex, self.vertexList[v[0]])

    def areVertexConnected(self, vertexA, vertexB):
        vertexAIndex = self.vertexList.index(vertexA)
        vertexBIndex = self.vertexList.index(vertexB)
        for v in self.edgeList:
            if (v[0] == vertexAIndex and v[1] == vertexBIndex) or (v[1] == vertexAIndex and v[0] == vertexBIndex):
                return True

        return False


a = -1

g = VertexList()
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
    print "Edge List (Graphs)"
    a = input("Choose an option: ")

    if a == 1:
        pass



