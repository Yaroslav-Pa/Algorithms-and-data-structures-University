class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addAfter(self, prevNode, data):
        if prevNode is None:
            return
        new_node = Node(data)
        new_node.next = prevNode.next
        prevNode.next = new_node
        new_node.prev = prevNode
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

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
        self._heapifyUp(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapifyDown(0)
        return root

    def _heapifyUp(self, index):
        while index > 0:
            parentIndex = (index - 1) // 2
            if self.heap[index] < self.heap[parentIndex]:
                self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
                index = parentIndex
            else:
                break

    def _heapifyDown(self, index):
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2
        smallest = index

        if leftChildIndex < len(self.heap) and self.heap[leftChildIndex] < self.heap[smallest]:
            smallest = leftChildIndex
        if rightChildIndex < len(self.heap) and self.heap[rightChildIndex] < self.heap[smallest]:
            smallest = rightChildIndex

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapifyDown(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self._heapifyDown(i)

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


# def heapSort(arr):
#     priorityQueue = PriorityQueue()
#     for item in arr:
#         priorityQueue.insert(item)
#     sortedArr = []
#     while True:
#         item = priorityQueue.remove()
#         if item is None:
#             break
#         sortedArr.append(item)
#     return sortedArr


if __name__ == "__main__":
    print("\nDoubly Linked List:")
    linkedList = DoublyLinkedList()
    linkedList.addToBeginning(9)
    linkedList.addToBeginning(5)
    linkedList.addToBeginning(1)
    linkedList.addToBeginning(2)
    linkedList.addAfter(linkedList.findNode(5), 4)
    linkedList.displayFromStart()
    linkedList.deleteNode(linkedList.findNode(1))
    linkedList.displayFromStart()
    linkedList.displayFromEnd()

    print("\nPriority Queue:")
    priorityQueue = PriorityQueue()
    arr = [9, 7, 5, 2, 10, 1]
    for item in arr:
        priorityQueue.insert(item)
    priorityQueue.display()
    sortedArr = priorityQueue.sort()
    print("Sorted Array:", sortedArr)
    unsortedArr = [4, 8, 2, 6, 7, 1]
    priorityQueue.buildHeap(unsortedArr)
    print("Sorted Array:")
    priorityQueue.display()

    # print("\nSort:")
    # arr2 = [7, 3, 1, 5, 9, 2]
    # sortedArr = heapSort(arr2)
    # print(sortedArr)
