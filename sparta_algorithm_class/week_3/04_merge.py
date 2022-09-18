array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    merge_arr = []
    index_a = 0
    index_b = 0
    while index_a < len(array1) and index_b < len(array2):
        if array1[index_a] < array2[index_b]:
            merge_arr.append(array1[index_a])
            index_a += 1
        elif array1[index_a] > array2[index_b]:
            merge_arr.append(array2[index_b])
            index_b += 1

    if index_a == len(array1): # index_b가 남았다는 의미이기 때문에
        while index_b < len(array2):
            merge_arr.append(array2[index_b])
            index_b += 1
    if index_b == len(array2):
        while index_a < len(array1):
            merge_arr.append(array1[index_a])
            index_a += 1

    return merge_arr


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!