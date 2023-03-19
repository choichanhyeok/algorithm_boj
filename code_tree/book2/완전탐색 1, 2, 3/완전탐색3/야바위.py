n = int(input())
yabawi = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = -1
for stone_idx in range(1, 4):
    table = [False] * 4
    table[stone_idx] = True
    correct_count = 0

    for i in range(n):
        a, b, c = tuple(yabawi[i])
        table[a], table[b] = table[b], table[a]

        if table[c]:
            correct_count += 1

    answer = max(answer, correct_count)

print(answer)



# 3개의 종이컵이 안쪽에 무엇이 들었는지 보이지 않도록 뒤집혀 있고, 셋 중 하나에 조약돌을 넣어 놓고 게임을 진행하려 합니다. N번에 걸쳐 a번 종이컵과 b번 종이컵을 교환한 뒤, c번 종이컵을 열어 그 안에 조약돌이 있으면 점수를 얻는 행동을 반복한다 할때, 처음 조약돌을 어디에 넣어야 가장 높은 점수를 얻을 수 있는지를 계산하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에는 N이 주어집니다.
#
# 그 다음 줄 부터는 N개의 줄에 걸쳐 한 줄에 하나씩 a, b, c값이 공백을 사이에 두고 주어집니다.
#
# 1 ≤ N ≤ 100
# 1 ≤ a, b, c ≤ 3, a ≠ b
# 출력 형식
# 첫 번째 줄에 처음 조약돌을 넣을 종이컵을 잘 선택하여 N번 시행 이후 얻을 수 있는 최대 점수를 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 3
# 1 2 1
# 3 2 1
# 1 3 1
# 출력:
#
# 2