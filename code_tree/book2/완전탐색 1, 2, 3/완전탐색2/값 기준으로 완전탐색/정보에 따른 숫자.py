import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
t, a, b = tuple(map(int, input().split()))

sn_data = [
    tuple(input().split())
    for _ in range(t)
]

ans = 0

# 각 숫자에 대해
# s에 더 가까운지 n에 더 가까운지 판단합니다.
for i in range(a, b + 1):
    # 숫자 i에서부터 s로부터의 거리와
    # n으로부터의 거리를 확인합니다.
    distance_s = INT_MAX
    distance_n = INT_MAX

    for p, q in sn_data:
        q = int(q)

        if p == 'S':
            distance_s = min(distance_s, abs(q - i))
        else:
            distance_n = min(distance_n, abs(q - i))

    if distance_s <= distance_n:
        ans += 1

print(ans)


# 1차 수직선 상에 T개의 알파벳이 놓여있습니다. 알파벳은 S, N으로만 주어지며, 특정 위치 x = k로부터 가장 가까이에 있는 알파벳 S까지의 거리 d1이 x = k로부터 가장 가까이에 있는 알파벳 N까지의 거리 d2보다 같거나 작은 경우 x = k는 특별한 위치가 됩니다. x = a부터 x = b까지의 위치 중 특별한 위치의 수를 구하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 T, a, b가 공백을 사이에 두고 주어집니다.
# 두 번째 줄부터는 T개의 줄에 걸쳐 각 알파벳 값 c와 해당 알파벳이 놓여있는 위치 x값이 공백을 사이에 두고 주어집니다. 알파벳은 S혹은 N으로만 주어지며, 주어지는 x 좌표는 전부 다름을 가정해도 좋습니다. 또, 알파벳 S, N은 최소 1개 이상씩 주어짐을 가정해도 좋습니다.
#
# 2 ≤ T ≤ 100
# 1 ≤ a ≤ b ≤ 1,000
# 출력 형식
# 첫 번째 줄에 조건을 만족하는 위치의 개수를 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 3 1 10
# S 10
# N 4
# S 1
# 출력:
#
# 6
# 예제 설명
# 1이상 10이하의 위치값 중 x = 1, 2, 7, 8, 9, 10만이 특별한 위치가 됩니다. 따라서 답은 6이 됩니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB