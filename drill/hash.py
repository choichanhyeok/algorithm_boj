

# class Dict:
#     def __init__(self):
#         self.items = [None] * 8
#
#     def put(self, key, value):
#         index = hash(key) % len(self.items) # index 만들기: key값을 hash로 돌린 뒤 배열의 길이 만큼 나눠서 만들 수 있다.
#         self.items[index] = value           # 해당 key의 index에 value값 저장
#
#     def get(self, key):
#         index = hash(key) % len(self.items) # 입력받은 key값을 hash 돌려서 배열 길이로 나눠 index 찾기
#         return self.items[index]            # 해당 index의 value를 리턴해주면 된다.


class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    # 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
    # 현재 self.items[2] 가 [("slow", "느린")] 이었다!
    # 그렇다면 새로 넣는 key, value 값을 뒤에 붙여주자!
    # self.items[2] == [("slow", "느린") -> ("fast", "빠른")] 이렇게!

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

    # 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
    # 현재 self.items[2] 가 [("slow", "느린") -> ("fast", "빠른")] 이었다!
    # 그렇다면 그 리스트를 돌면서 key 가 일치하는 튜플을 찾아준다.
    # ("fast", "빠른") 이 일치하므로 "빠른" 이란 값을 돌려주자!






#
# class LinkedTuple:
#     def __init__(self):
#         self.items = []
#     def add(self, key, value):
#         self.items.append((key, value))
#     def get(self, key):
#         for k, v in self.items:
#             if k == key:
#                 return v
#
#
# class LinkedDict:
#     def __init__(self):
#         self.items = []
#         for i in range(8):
#             self.items.append(LinkedTuple())
#
#     def put(self, key, value):
#         index = hash(key) % len(self.items)
#         self.items[index].add(key, value)
#         return
#
#     def get(self, key):
#         index = hash(key) % len(self.items)
#         return self.items[index].get(key)
#
# my_dict = LinkedDict()
# my_dict.put("test", 3)
# print(my_dict.get("test"))
