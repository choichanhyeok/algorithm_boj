

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return "stack is empty. you can't using pop()."
        delete_data = self.head.value
        self.head = self.head.next

        return delete_data

    def is_empty(self):
        return self.head is None
    def peek(self):
        return self.head.value



# #TODO 1. Node를 만들어야 함. 이유는? 데이터 뿐 아니라 연관 노드의 주소도 저장하기 위해서
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#
#     def pop(self):
#         if self.is_empty():
#             return "this stack is empty. you can't using pop()"
#
#         delete_data = self.head.value
#         self.head = self.head.next
#         return delete_data
#     def is_empty(self):
#         return self.head is None
#
#     def peek(self):
#         return self.head.value

# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.head = None
#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#
#     def pop(self):
#         #TODO 1. 스택의 맨 위 노드를 그냥 재껴주는거거덩요 ? (단, stack이 None 이 아닐때)
#         if stack is None:
#             return "스택이 비어있습니다. 비어있는 스택에 대해서 pop()할 수 없습니다."
#
#         pop_data = self.head.data
#         self.head = self.head.next
#         return f"pop success {pop_data}"
#     def is_empty(self):
#         return self.head is None
#
#     def peek(self):
#         return self.head.data


# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     #TODO 1: push
#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#
#     #TODO 2: pop
#     def pop(self):
#         if self.is_empty():
#             return "the Stack is Empty, can\'t apply pop"
#         delete_node = self.head
#         self.head = self.head.next
#
#         return delete_node.data
#
#
#     #TODO 3: peek
#     def peek(self):
#         return self.head.data
#
#     #TODO 4: isEmpty
#     def is_empty(self):
#         return self.head is None
#




stack = Stack()
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.peek())
stack.pop()
print(stack.is_empty())
















# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, value):
#         # 어떻게 하면 될까요?
#         return
#
#     # pop 기능 구현
#     def pop(self):
#         # 어떻게 하면 될까요?
#         return
#
#     def peek(self):
#         # 어떻게 하면 될까요?
#         return
#
#     # isEmpty 기능 구현
#     def is_empty(self):
#         # 어떻게 하면 될까요?
#         return
#
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, value):
#         new_head = Node(value)
#         new_head.next = self.head
#         self.head = new_head
#
#     # pop 기능 구현
#     def pop(self):
#         if self.is_empty():
#             return "Stack is Empty"
#         delete_head = self.head
#         self.head = self.head.next
#
#         return delete_head
#
#     def peek(self):
#         if self.is_empty():
#             return "Stack is Empty"
#         return self.head.data
#
#     # isEmpty 기능 구현
#     def is_empty(self):
#         return self.head is None

#
# stack = Stack()
# stack.push(3)
# print(stack.peek())
# stack.push(4)
# stack.push(5)
# print(stack.peek())
# print(stack.pop())
# print(stack.peek())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.peek())

