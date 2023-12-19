from timeit import default_timer as timer
from variables1 import DoublLinkList
from variables1 import PriorityQueue as arr

class Node: # вузол
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addAfter(self, prevNode, data):
        if prevNode is None:
            return
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next:
            newNode.next.prev = newNode
        else:
            self.tail = newNode

    def findNode(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def deleteNode(self, node):
        if node is None:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def displayFromStart(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def displayFromEnd(self):
        current = self.tail
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.heapifyUp(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root

    def heapifyUp(self, index):
        while index > 0:
            parentIndex = (index - 1) // 2
            if self.heap[index] < self.heap[parentIndex]:
                self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
                index = parentIndex
            else:
                break

    def heapifyDown(self, index):
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2
        smallest = index

        if leftChildIndex < len(self.heap) and self.heap[leftChildIndex] < self.heap[smallest]:
            smallest = leftChildIndex
        if rightChildIndex < len(self.heap) and self.heap[rightChildIndex] < self.heap[smallest]:
            smallest = rightChildIndex

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapifyDown(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self.heapifyDown(i)

    def sort(self):
        sortedArr = []
        while True:
            item = self.remove()
            if item is None:
                break
            sortedArr.append(item)
        return sortedArr

    def display(self):
        for item in self.heap:
            print(item, end=' ')
        print()


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    print("\nDoubly Linked List:")
    
    linkedList = DoublyLinkedList()
    linkedList.addToBeginning(DoublLinkList[0])
    linkedList.addToBeginning(DoublLinkList[1])
    linkedList.addToBeginning(DoublLinkList[2])
    linkedList.addToBeginning(DoublLinkList[3])
    print("Adding 4 after 5:")
    linkedList.addAfter(linkedList.findNode(5), 4)
    linkedList.displayFromStart()
    print("Deleted 1")
    linkedList.deleteNode(linkedList.findNode(1))
    print("Display from start\end:")
    linkedList.displayFromStart()
    linkedList.displayFromEnd()

    print("\nPriority Queue:")
    priorityQueue = PriorityQueue()
    
    for item in arr:
        priorityQueue.insert(item)
    priorityQueue.display()
    sortedArr = priorityQueue.sort()
    print("Sorted Array:", sortedArr)

    startTime = timer()
    priorityQueue.buildHeap(arr)
    endTime = timer()
    print("Heap Array:")
    priorityQueue.display()    
    
    startTime1 = timer()
    bubbleSort(arr)
    endTime1 = timer()

    print("Time taken (heap):", endTime - startTime, "s")
    print("Time taken (bubble):", endTime1 - startTime1, "s")
    
