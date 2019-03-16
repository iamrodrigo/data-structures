class AdjacencyMatrix(object):
    def __init__(self):
        self.vertexList = []
        self.edgeMatrix = []
        self.numberOfVertex = 0

    def createVertex(self, value):
        self.vertexList.append(value)
        newArray = [0 for _ in self.vertexList]

        for list in self.edgeMatrix:
            list.append(0)

        self.edgeMatrix.append(newArray)

    def connectVertices(self, vertexA, vertexB):
        vertexAIndex = self.vertexList.index(vertexA)
        vertexBIndex = self.vertexList.index(vertexB)

        self.edgeMatrix[vertexAIndex][vertexBIndex] = 1
        self.edgeMatrix[vertexBIndex][vertexAIndex] = 1

    def findAdjacentVertex(self, vertex):
        vertexIndex = self.vertexList.index(vertex)
        for i, v in enumerate(self.edgeMatrix[vertexIndex]):
            if v:
                print "Vertex {} is connected with vertex {}".format(vertex, self.vertexList[i])

    def areVertexConnected(self, vertexA, vertexB):
        vertexAIndex = self.vertexList.index(vertexA)
        vertexBIndex = self.vertexList.index(vertexB)

        return True if self.edgeMatrix[vertexAIndex][vertexBIndex] else False

a = -1

g = AdjacencyMatrix()
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
    print "Adjacency Matrix (Graphs)"
    a = input("Choose an option: ")

    if a == 1:
        pass



