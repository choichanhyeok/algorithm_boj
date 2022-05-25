# 카드 합이 21을 넘지 않는 한도 안에서, 카드의 합을 최대한 크게 만드는 게임
# 규정은 게임마다 다름
# 김정인, 상근-창영이랑 게임 할건데
# 조건: 각 카드에는 양수, 딜러는 N장의 카드를 모두 숫자가 보이게 바닥에 놓음, 3장을 뽑아 딜러가 외치는 M에 가장 가깝게 만들어야함
# 최적 조건: 가장 큰 수 3가지를 더하면, 가장 큰 합이 나온다.
   # + 방법1: 정렬 이후, 맨 뒤에서 3개
   # + 방법2: max로 가장 큰 값 구하고, 해당 값 소거 => 3번 반복

# # 카드 개수 N과 목표 카드 점수 M
# n, m = map(int, input().split(' '))
# card_list = list(map(int, input().split(' ')))
# card_list.sort()
# print(card_list)
# for i in range(1, m-3):
#     if (card_list[-1*i] + card_list[(-1*i)-1] + card_list[(-1*i)-2]) <= m:
#         print(card_list[-1*i] + card_list[(-1*i)-1] + card_list[(-1*i)-2])
#         break



# n, m = list(map(int, input().split(' ')))
# data = list(map(int, input().split(' ')))
#
# result = 0
# length = len(data)
#
# for i in range(0, length):
#     for j in range(i + 1, length):
#         for k in range(j + 1, length):
#             sum_value = data[i] + data[j] + data[k]
#             if sum_value <= m:
#                 print(data[i], data[j], data[k])
#                 result = max(result, sum_value)
# print(result)


n, m = map(int, input().split(' '))
card_list = list(map(int, input().split(' ')))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_value = card_list[i] + card_list[j] + card_list[k]
            if sum_value < m:
                result = max(sum_value, result)
print(result)


