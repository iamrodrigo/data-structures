class MinHeap(object):
    def __init__(self, arrayList = []):
        self.arrayList = arrayList
        self.heapify()

    def insert(self, n):
        self.arrayList.append(n)
        actualPosition = len(self.arrayList) - 1
        parent = (actualPosition - 1) / 2

        while actualPosition > 0 and self.arrayList[parent] > self.arrayList[actualPosition]:
            self.arrayList[parent], self.arrayList[actualPosition] = self.arrayList[actualPosition], self.arrayList[parent]
            actualPosition = parent
            parent = (actualPosition - 1) / 2

    def minHeapify(self, i, length = 0):
        length = length if length else len(self.arrayList)
        left = (2 * i) + 1
        right = left + 1

        while left < length:
            if self.arrayList[i] > self.arrayList[left] or length > right and self.arrayList[i] > self.arrayList[right]:
                minChild = right if right < length and self.arrayList[left] > self.arrayList[
                    right] else left
                self.arrayList[minChild], self.arrayList[i] = self.arrayList[i], self.arrayList[minChild]
                i = minChild

                left = (2 * i) + 1
                right = left + 1
            else:
                break

    def extract(self):
        if not len(self.arrayList):
            return None
        if len(self.arrayList) == 1:
            return self.arrayList.pop()
        else:
            i = 0
            first = self.arrayList[0]
            self.arrayList[0] = self.arrayList.pop()
            self.minHeapify(i)
            return first

    def heapify(self):
        for i in xrange((len(self.arrayList) / 2) - 1, -1, -1):
            self.minHeapify(i)

    def heapSort(self):
        for i in xrange(len(self.arrayList) -1, 0, -1):
            if self.arrayList[0] == 39:
                pass
            self.arrayList[i], self.arrayList[0] = self.arrayList[0], self.arrayList[i]
            self.minHeapify(0, i)

h = MinHeap([45, 44, 43, 42, 41, 40, 39, 38, 37])
h.heapSort()
#h.insert(8)
#h.insert(18)
#h.insert(10)
#h.insert(20)
#h.insert(28)
#h.insert(39)
#h.insert(29)
#h.insert(37)
#h.insert(26)
#h.insert(76)
#h.insert(1)
#h.insert(3)
#h.insert(5)
#h.insert(4)
print h.arrayList
#print h.extract()
#print h.extract()


