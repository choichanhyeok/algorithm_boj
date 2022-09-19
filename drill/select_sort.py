


input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 채워 넣으세요
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))





#
#
# #key1: (n-i)로 내림차순시, i + j로 접근 가능
# #key2: 버블 정렬이랑 거의 비슷, 단. 이웃간의 스윕이 아니라 최소값 사이의 스웝
#
#
#
# #key1:
# # - line1:    4, 6, 2, 9, 1           = min if  ~~~
# # 와! 1이다!   1, 4, 6, 2, 9
# # - line2:  1, <-    4, 6, 2, 9
# #               @ ~~~
#
# def selection_sort(array):
#     n = len(array)
#
#     # 1. 리스트의 처음부터 끝까지 순회하면서, 최소값을 찾는다.
#     # 2. 최소값을 순회의 시작점과 swap한다.
#     # 3. 맨 앞에는 정렬된 상태!, 다음 순회는 현재의 맨 앞을 i라고 할 때 i+1로 하도록 해야한다.
#     # 4. 반복,
#
#     for i in range(n-1):
#         min_index = i
#         for j in range(n-i):
#             if array[i+j] < array[min_index]:
#                 min_index = i+j
#         array[min_index], array[i] = array[i], array[min_index]
#     return array
#
#
#
# def bubble_sort(array):
#     n = len(array)
#
#     # key1: 이웃하는 놈들끼리 swap
#     # key2: 맨 뒤에 정렬합니다.
#
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array
#
#
# # def selection_sort(array):
# #     n = len(array)
# #
# #     # key1. 정렬된 요소를 맨 앞에 두고, 탐색 범위를 한칸 위로 올린다
# #     # key2. swap은 하나의 작업의 단위가 끝난 뒤 (여기서 작업의 단위란 리스트의 i~ end index까지 최소값을 찾는 작업)
# #
# #
# #     for i in range(n-1):
# #         min_index = i
# #         for j in range(n-i):
# #             if array[i+j] < array[min_index]:
# #                 min_index = i+j
# #         array[i], array[min_index] = array[min_index], array[i]
# #
# #     return array
#
#
#
#
# #keywor1: 이웃 Swap
# #keyword2: 맨 뒤에다 박아줘,
#
# # def bubble_sort(array):
# #     n = len(array)
# #
# #     for i in range(n-1):
# #         for j in range(n-i-1):
# #             if array[j] > array[j+1]:
# #                 array[j], array[j+1] = array[j+1], array[j]
# #
# #     return array
#
#
#
#
# # def selection_sort(array):
# #     n = len(array)
# #
# #     for i in range(n-1):
# #         min_index = i
# #         for j in range(n-i):    # i 값이 계속 올라가니까, 줄여줘
# #             if array[i+j] < array[min_index]:
# #                 min_index = i + j
# #         array[i], array[min_index] = array[min_index], array[i]
# #
# #     return array
#
#
# selection_sort(input)
# print(input)
#
# print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
# print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
# print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))