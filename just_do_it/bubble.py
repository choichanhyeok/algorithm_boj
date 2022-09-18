

target_list = [3, 5, 2 ,7, 1]





# 버블 정렬
# key1. 버블은 뽀글뽀글, swap을 통해 pivot이 이동해.
# key2. 두 요소중 큰 요소를 뒤로 계속 밀어서 맨 뒤로 보낸다음, 다음 탐색에서는 맨 뒤를 탐색 안하도록 길이-i를 해주면 돼(오름차순 기준)


# 버블정렬 2개만 기억하면돼.
# 1. 스왑한다
# 2. 정렬된 요소를 맨 뒤에 박아놓고, 다음 정렬에선 맨 뒤를 -i 해주면 된다. (여기서 i가 증가하도록)



# 1. 스왑
# 2. 맨 뒤에 박아놓고 -i로 탐색 범위 줄이기

for i in range(len(target_list)):
    for j in range(len(target_list)-i-1):
        if target_list[j] > target_list[j+1]:
            target_list[j], target_list[j+1] = target_list[j+1], target_list[j]

print(target_list)


# for i in range(len(target_list)):
#     for j in range(len(target_list)-i-1):
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)

# for i in range(len(target_list)):
#     for j in range(len(target_list)-i-1):
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)


# for i in range(len(target_list)):
#     for j in range(len(target_list)-i-1):
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)



# for i in range(len(target_list)):
#     for j in range(len(target_list)-i-1):
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)

## 복잡도: O(N^2)



# # drill 2. 2022-09-18
# for i in range(len(target_list)):         # i의 최대는 0인 경우
#     for j in range(len(target_list)-i-1): # target[5]에 접근하는 경우가 발생, 고로 -i를 해줘야 하고
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)


# # drill 1. 2022-09-18
# for i in range(len(target_list)):
#     for j in range(len(target_list)-i-1):
#         if target_list[j] > target_list[j+1]:
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
# 
# print(target_list)


# for i in range(len(target_list)):                       # >> i = for 0, 1, 2, 3, 4
#     for j in range(len(target_list)-i-1):               # >> j = for [5-0-1(4), 5-1-1(3), 5-2-1(2), 5-3-1(1), 5-4-1(0)]
#         if target_list[j] > target_list[j+1]:           #  target_list[j] => target_list[4] -> target_list[3] ~--~ target_list[0]
#             target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
#
# print(target_list)