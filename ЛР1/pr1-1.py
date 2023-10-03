class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_after(self, prev_node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def find_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete_node(self, node):
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

    def display_from_start(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def display_from_end(self):
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
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self._heapify_down(i)

    def sort(self):
        sorted_arr = []
        while True:
            item = self.remove()
            if item is None:
                break
            sorted_arr.append(item)
        return sorted_arr

    def display(self):
        for item in self.heap:
            print(item, end=' ')
        print()


def binary_heap_sort(arr):
    priority_queue = PriorityQueue()
    for item in arr:
        priority_queue.insert(item)
    sorted_arr = []
    while True:
        item = priority_queue.remove()
        if item is None:
            break
        sorted_arr.append(item)
    return sorted_arr


if __name__ == "__main__":
    print("\nDoubly Linked List:")
    linked_list = DoublyLinkedList()
    linked_list.add_to_beginning(9)
    linked_list.add_to_beginning(5)
    linked_list.add_to_beginning(1)
    linked_list.add_to_beginning(2)
    linked_list.add_after(linked_list.find_node(5), 4)
    linked_list.display_from_start()
    linked_list.delete_node(linked_list.find_node(1))
    linked_list.display_from_start()
    linked_list.display_from_end()

    print("\nPriority Queue:")
    priority_queue = PriorityQueue()
    arr = [9, 7, 5, 2, 10, 1]
    for item in arr:
        priority_queue.insert(item)
    priority_queue.display()
    sorted_arr = priority_queue.sort()
    print("Sorted Array (Heap sort):", sorted_arr)
    unsorted_arr = [4, 8, 2, 6, 7, 1]
    priority_queue.build_heap(unsorted_arr)
    priority_queue.display()

    print("\n Binary Heap sort")
    arr2 = [7, 3, 1, 5, 9, 2]
    sorted_arr = binary_heap_sort(arr2)
    print(sorted_arr)
