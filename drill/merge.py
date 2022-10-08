





# 두 array를 비교하며 작은 것을 넣어준다.
def merge(array1, array2):
    array1_index = 0
    array2_index = 0
    result = []


    # TODO1. 두 배열의 각 요소들을 비교하며 작은 값들을 result에 추가
    while array1_index != len(array1) and array2_index != len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1

        else:
            result.append(array2[array2_index])
            array2_index += 1


    # TODO2. 다 비워지지 않은 배열의 요소를 result에 append
    if array1_index == len(array1):
        while array2_index != len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index != len(array1):
            result.append(array1)
            array1_index += 1

    return result




# def merge(array1, array2):
#     #TODO 1. 두 array를 순회하면서 작은 거 먼저
#     array1_index = 0
#     array2_index = 0
#
#     result = []
#
#     while array1_index != len(array1) and array2_index != len(array2):
#         if array1[array1_index] < array2[array2_index]:
#             result.append(array1[array1_index])
#             array1_index += 1
#         else:
#             result.append(array2[array2_index])
#             array2_index += 1
#
#
#     if array1 == len(array1):
#         while array2_index != len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#     if array2 == len(array2):
#         while array1_index != len(array1):
#             result.append(array1[array1_index])
#             array1_index += 1
#     return result



# def merge(array1, array2):
#     array1_index = 0
#     array2_index = 0
#     result = []
#
#     while array1_index != len(array1) and array2_index != len(array2):
#         if array1[array1_index] < array2[array2_index]:
#             result.append(array1[array1_index])
#             array1_index += 1
#         else:
#             result.append(array2[array2_index])
#             array2_index += 1
#
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




array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


# def merge(array1, array2):
#     # 채워 넣으십쇼
#     return


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))





































# array_a = [1, 2, 3, 5]
# array_b = [4, 6, 7, 8]
#
#
# def merge(array1, array2):
#     result = []
#     array1_index = 0
#     array2_index = 0
#
#     while array1_index < len(array1) and array2_index < len(array2):
#         if array1[array1_index] < array2[array2_index]:
#             result.append(array1[array1_index])
#             array1_index += 1
#
#         else:
#             result.append(array2[array2_index])
#             array2_index += 1
#
#     if array1_index == len(array1):
#         while array2_index != len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#     if array2_index == len(array2):
#         while array1_index != len(array1):
#             result.append(array1[array1_index])
#             array1_index += 1
#
#     return result



# def merge(array1, array2):
#     result = []
#     array1_index = 0
#     array2_index = 0
#
#
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


print(merge(array_a, array_b))

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))