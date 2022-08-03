# TODO: 간단한 링크드 리스트 예제

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)          #
        if index == 0:                  # case1. 제일 앞에 넣고 싶을 때,
            new_node.next = self.head   # new_node에 next에 head를 넣어줌,
            self.head = new_node        # 헤드 값을 새로운 노드로 교체
            return

        node = self.get_node(index - 1) # case2. 타겟으로 하는 index의 전 노드를 받아옴
        next_node = node.next           # 이전 노드의 next 값 (기존 i+1)을 next_node에 넣음
        node.next = new_node            # 이전 노드의 next 값을 지금 add한 노드로 변경
        new_node.next = next_node       # 지금 add한 노드의 next에 (기존 i+1)노드의 값을 넣어줌

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index -1)
        prev_node.next = prev_node.next.next
        return


linked_list = NodeMgmt(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()