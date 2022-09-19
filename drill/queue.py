

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "the deque is empty"

        delete_node = self.head
        self.head = self.head.next

        return delete_node.data

    def peek(self):
        if self.is_empty():
            return "the Deque id empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
