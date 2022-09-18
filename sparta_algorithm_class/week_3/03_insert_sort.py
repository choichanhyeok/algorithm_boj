input = [4, 6, 2, 9, 1]

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

insertion_sort(input)
print(input)

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))


# 빅오는 선택, 버블과 같은 O(N^2)이지만, 오메가로 봤을 땐 O(N)이 된다. 이미 정렬이 많이 진행된 구문의 경우 효과가 커진다.