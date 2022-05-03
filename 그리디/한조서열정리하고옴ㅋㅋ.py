
# https://www.acmicpc.net/problem/14659

# 분석 #
# 일단 모든 케이스를 봐야 계산 가능, 특별한 공식 없어보임 #



n = int(input())
hill_list = list(map(int, input().split()))

#max = 0
#temp_sum = 0
#pivot = hill_list[0]
#for i in range(1, n):
#    if pivot >= hill_list[i]:
#        temp_sum += 1
#    else:
#        pivot = hill_list[i]
#        if max < temp_sum:
#            max = temp_sum
#            temp_sum = 0
#if max < temp_sum:
#    max = temp_sum
#print(max)

n = int(input())
hill_list = list(map(int, input().split()))

res = 0
highest=0
cnt=0

for hill in hill_list:
    if hill > highest:
        highest = hill
        cnt = 0
    else:
        cnt += 1
    res = max(res, cnt)

print(res)

