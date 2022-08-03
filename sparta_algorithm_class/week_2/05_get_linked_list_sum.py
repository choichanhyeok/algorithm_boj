class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def get_linked_list_array(cur):
    nsum = 0
    while cur is not None:
        nsum = nsum * 10 + cur.data
        cur = cur.next
    return nsum

#TODO: 입력값으로 들어오는 두 리스트의 합을 구하라. 단, 각 요소의 합으로 계산해야 한다.  323 + 625 = 948
def get_linked_list_sum(linked_list_1, linked_list_2):
    '''

    :param linked_list_1:
    :param linked_list_2:
    :return:
    '''
    cur_1 = linked_list_1.head
    cur_2 = linked_list_2.head

    nsum1 = get_linked_list_array(cur_1)
    nsum2 = get_linked_list_array(cur_2)

    return nsum1 + nsum2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
