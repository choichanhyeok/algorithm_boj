
array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):

    # exit case
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left_array = array[:mid]
    right_array = array[mid:]

    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(array1, array2):
    array1_index = 0
    array2_index = 0
    result = []

    #TODO 1. 배열의 각 요소 순회하면서 작은 값들을 result에 집어넣음
    while array1_index != len(array1) and array2_index != len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    #TODO 2. 모든 값이 추출되지 못한 배열을 순서대로 result에 append (merger sort는 각 배열이 정렬된 상태임을 가정하기 때문에)
    if array1_index == len(array1):
        while array2_index != len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index != len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!



# array = [5, 3, 2, 1, 6, 8, 7, 4]
#
#
#
#
# def merge_sort(array):
#     if len(array) <= 1:
#         return array # exit sentence
#
#     mid = len(array)//2
#     left_array = array[:mid]
#     right_array = array[mid:]
#
#     return merge(merge_sort(left_array), merge_sort(right_array))
#
#
#
# def merge(array1, array2):
#     array1_index = 0
#     array2_index = 0
#     result = []
#
#     while array1_index != len(array1) and array2_index != len(array2):
#         #TODO 1: 두 배열의 각 요소 (_index)중 작은 거를 result에 추가토록
#         if array1[array1_index] < array2[array2_index]:
#             result.append(array1[array1_index])
#             array1_index += 1
#         else:
#             result.append(array2[array2_index])
#             array2_index += 1
#
#     #TODO 2: 두 배열중, 남은 애들은 그냥 result에 추가토록 하면 됌
#     if array1_index == len(array1):
#         while array2_index != len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#
#     if array2_index == len(array2):
#         while array1_index != len(array1):
#             result.append(array1[array1_index])
#             array1_index += 1
#
#     return result
#
# print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!








#
#
#
#
#
#
# def merge_sort(array):
#     if len(array) <= 1:
#         return array
#
#     mid = len(array)//2
#     left_array = array[:mid]
#     right_array = array[mid:]
#
#     return merge(merge_sort(left_array), merge_sort(right_array))
#
#
#
# array = [5, 3, 2, 1, 6, 8, 7, 4]
#
#
# # def merge_sort(array):
# #     # 여기 적으시오
# #     return array
#
#
# def merge(array1, array2):
#     result = []
#     array1_index = 0
#     array2_index = 0
#     while array1_index < len(array1) and array2_index < len(array2):
#         if array1[array1_index] < array2[array2_index]:
#             result.append(array1[array1_index])
#             array1_index += 1
#         else:
#             result.append(array2[array2_index])
#             array2_index += 1
#
#     if array1_index == len(array1):
#         while array2_index < len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#
#     if array2_index == len(array2):
#         while array1_index < len(array1):
#             result.append(array1[array1_index])
#             array1_index += 1
#
#     return result
#
#
# print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
#
# print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
# print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
# print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))
#
#



















# array = [5, 3, 2, 1, 6, 8, 7, 4]
#
#
# # def merge_sort(array):
# #     if len(array) <= 1:
# #         return array
# #
# #     mid = len(array) // 2
# #     left_array = array[:mid]
# #     right_array = array[mid:]
# #
# #     return merge(merge_sort(left_array), merge_sort(right_array))
#
#
# def merge_sort(array):
#     if len(array) <= 1:
#         return array
#
#     mid = len(array)//2
#     left_array = array[:mid]
#     right_array = array[mid:]
#
#     return merge(merge_sort(left_array), merge_sort(right_array))
#
# def merge(array1, array2):
#     result = []
#     array1_index = 0
#     array2_index = 0
#     while array1_index < len(array1) and array2_index < len(array2):
#         if array1[array1_index] < array2[array2_index]:
#             result.append(array1[array1_index])
#             array1_index += 1
#         else:
#             result.append(array2[array2_index])
#             array2_index += 1
#
#     if array1_index == len(array1):
#         while array2_index < len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#
#     if array2_index == len(array2):
#         while array1_index < len(array1):
#             result.append(array1[array1_index])
#             array1_index += 1
#
#     return result
#
#
#
# print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
#
# print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
# print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
# print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))