target_list = [4, 5, 2, 3, 9, 10, 11, 5, 3, 3, 16, 3002]



# 버블 정렬은?
# 전체 순회를 하면서 피봇(j)과 비교 대상(j+1)을 비교
# 만약 j가 더 클시 j+1과 위치 변경
# 이렇게 모든 위치의 비교를 통해 O(N^2)의 작업을 진행한다.



def bubble_sort(array):
    n = len(array)

    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array



# def bubble_sort(array):
#     n = len(array)
#
#     for i in range(n-1):
#         for j in range(n-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array



# def bubble_sort(array):
#     n = len(array)
#
#     for i in range(n-1):
#         for j in range(n-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array


# def bubble_sort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-1):
#             array[j], array[j+1] = array[j+1], array[j]
#
#     return array




# def bubble_sort(array):
#     n = len(array)
#
#     for i in range(n-1):
#         for j in range(n-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#     return array







# drill set
input = [4, 6, 2, 9, 1]


# def bubble_sort(array):
#     # 여기서 부터
#     return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))






# # drill set
# input = [4, 6, 2, 9, 1]
#
#
# def bubble_sort(array):
#     # 이 부분을 채워보세요!
#     return array
#
#
# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
#
# print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
# print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
# print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))

































## 1. swap
## 2. 정렬된 요소 맨 뒤에다 박아놓고 탐색 범위를 하나씩 줄이는데, 이거를 자동으로 해주기 위해서 -i해준다.


count = 0
for i in range(len(target_list)-1):
    for j in range(len(target_list)-i-1):
        count += 1
        if target_list[j] > target_list[j+1]:
            target_list[j], target_list[j+1] = target_list[j+1], target_list[j]

print(target_list)
print(count)


# for i in range(len(target_list)):
#     for j in range(len(target_list)-i-1):
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)


# for i in range(len(target_list)):
#     try:
#         for j in range(len(target_list)-i-1):
#             if target_list[j] > target_list[j+1]:
#                 target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#     except:
#         print(f'j값: {j}\n i값: {i}')
#         print(len(target_list)-i)
#
# print(target_list)



#
# for i in range(len(target_list)):
#     for j in range(len(target_list)-i-1):
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)