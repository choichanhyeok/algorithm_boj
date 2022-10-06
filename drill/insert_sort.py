

input = [4, 6, 2, 9, 1]

# 조건1. pivot(i)는 하나씩 증가하며 정렬한다.
# 조건2. 따라서 탐색을 할 j의 범위는 0~i까지이다.
# 조건3. 그럼 i에서 -1까지의 순회는 어떻게 하느냐?, 다양한 방법이 있겠지만 i-j와 i-j-1의 비교를 하면 된다.
# 조건4. 자기보다 작은 값이 나오면 순회를 중단한다. (이미 정렬된 리스트이기 때문에)




# 삽입 정렬은 i가 증가하면서 탐색 범위를 넓히며, 탐색 대상을 "삽입" 하는거
# 삽입 이후에 두 대상에 대해서 비교를 해야하는데, 비교는 역순으로 진행
# 이미 정렬된 리스트이기에 비교문이 false를 도출할때 break

def insertion_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
    return array



# def insertion_sort(array):
#     n = len(array)
#
#     for i in range(n):
#         for j in range(i):
#             if array[i-j] < array[i-j-1]:
#                 array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
#     return array



# def insertion_sort(array):
#     n = len(array)
#
#     for i in range(n):
#         for j in range(i):
#             if array[i-j] < array[i-j-1]:
#                 array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
#             else:
#                 break
#     return array



# def insertion_sort(array):
#     n = len(array)
#
#     for i in range(n):
#         for j in range(i):
#             if array[i-j-1] > array[i-j]:
#                 array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
#
#     return array


# def insertion_sort(array):
#         # 구현
#     return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))



























# def insertion_sort(array):
#     n = len(array)
#
#     for i in range(1, n):
#         for j in range(i):
#             if array[i-j] < array[i-j-1]:
#                 array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
#             else:
#                 break
#
#     return array
#
# input = [4, 6, 2, 9, 1]







#
#
# # 삽입 정렬
# # key1. break
# # key2. i-j-1
#
# def insertion_sort(array):
#     n = len(array)
#
#     for i in range(1, n):
#         for j in range(i):
#             if array[i-j-1] > array[i-j]:
#                 array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
#             else:
#                 break
#     return array
#
# # def insertion_sort(array):
# #     n = len(array)
# #     for i in range(1, n):
# #         for j in range(i):
# #             if array[i - j - 1] > array[i - j]:
# #                 array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
# #             else:
# #                 break
# #     return array
#
#
# insertion_sort(input)
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
#
# print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
# print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
# print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))