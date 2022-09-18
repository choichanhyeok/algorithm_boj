target_list = [4, 5, 2, 3, 9, 10, 11, 5, 3, 3, 16, 3002]


## 1. swap
## 2. 정렬된 요소 맨 뒤에다 박아놓고 탐색 범위 하나씩 줄이기 -i




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