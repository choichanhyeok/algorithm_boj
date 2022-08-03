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

    #TODO: 똑같은 링크드 리스트의 헤더를 2개 받는다. fast에 k만큼 링크를 순회한 후, fast의 next가 None이 될 때 까지 slow와 순회한댜.
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None: # fast는 목표인 k만큼 먼저 달렸으니까,
            slow = slow.next    # slow는 k만큼 덜 달리게 된다.
            fast = fast.next

        return slow


    # TODO: case2: 링크드리스트의 길이를 파악해, 길이-k로 뒤에서 k번째의 노드에 접근하는 방법  O(N+M)
    # def get_size_linked_list(self): #TODO: 해당 링크드리스트의 size를 구한다
    #     count = 0
    #     cur = self.head
    #     while cur is not None:
    #         cur = cur.next
    #         count += 1
    #     return count

    # def get_kth_node_from_last(self, k):  // 개선 전 모델
    #     list_size = self.get_size_linked_list()
    #
    #     #TODO: 맨 뒤에서 -k 번째의 인덱스를 긁어온다.
    #     cur = self.head
    #     for i in range(list_size-k):
    #         cur = cur.next
    #     return cur


linked_list = NodeMgmt(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!