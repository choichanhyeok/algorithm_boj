n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

arr_2d = [
    [0 for _ in range(max(arr))]
    for _ in range(n)
]

for i, elem in enumerate(arr):
    for j in range(elem):
        arr_2d[i][j] = 1

max_val = 0
for k in range(max(arr)):
    cnt = 0

    for l in range(n - 1):
        if (arr_2d[l][k] == 1 and arr_2d[l + 1][k] == 0):
            cnt += 1

    if arr_2d[n - 1][k] == 1:
        cnt += 1

    max_val = max(max_val, cnt)

print(max_val)


#
# 해수면의 높이에 따라 물에 잠기는 빙산들이 있습니다. 빙산의 개수 N이 주어지고 N개의 빙산들의 높이 H(i)가 순서대로 주어집니다. 빙산들이 물에 잠기지 않은 채로 붙어있는 경우를 한 덩어리로 볼 때, 해수면의 높이를 적절하게 설정 했을 때 가능한 빙산 덩어리의 최대 개수를 구하는 프로그램을 아래 예를 참고하여 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 빙산들의 개수 N이 주어지고
#
# 두 번째 줄부터 N개의 줄에 걸쳐 빙산의 높이 H(i)가 순서대로 한 줄에 하나씩 주어집니다.
#
# 1 ≤ N ≤ 100
# 1 ≤ H(i) ≤ 1,000
# 출력 형식
# 첫 번째 줄에 해당하는 값을 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 9
# 3
# 5
# 2
# 3
# 2
# 1
# 4
# 2
# 3
# 출력:
#
# 4