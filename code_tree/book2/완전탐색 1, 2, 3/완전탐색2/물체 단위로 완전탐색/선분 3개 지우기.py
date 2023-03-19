MAX_R = 100 + 1

n = int(input())
section = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


answer = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            line = [0] * MAX_R
            is_meet_something = False

            for idx in range(n):
                if idx == i or idx == j or idx == k:
                    continue
                x, y = section[idx]
                for l in range(x, y+1):
                    line[l] += 1

            for x in line:
                if 1 < x:
                    is_meet_something = True
                    break
            if not is_meet_something:
                answer += 1

print(answer)




# 1차원 직선 상에 n개의 선분이 주어집니다. 이 중 서로 다른 선분 3개를 제거하여 남은 n - 3개의 선분끼리 모두 겹쳐지지 않도록 하는 서로 다른 가짓수를 구하는 출력하는 프로그램을 작성해보세요. 단, 두 선분끼리 경계에서 닿는 경우 역시 겹치는 것으로 생각합니다.
#
# 입력 형식
# 첫 번째 줄에 n이 주어집니다.
#
# 두 번째 줄부터는 n개의 줄에 걸쳐 선분의 정보 (a, b)가 공백을 사이에 두고 주어집니다.
#
# 4 ≤ n ≤ 10
# 0 ≤ a < b ≤ 100
# 출력 형식
# 모두 겹쳐지지 않도록 하는 서로 다른 가짓수를 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 5
# 1 3
# 2 4
# 3 5
# 6 8
# 7 9
# 출력:
#
# 6
# 예제 설명
#
#
# 1, 2, 3번 선분 중에 2개를 제거하고, 4, 5번 선분 중에 1개를 제거해야만 모든 선분이 겹치지 않게 되므로 답은 3 * 2 = 6가지가 됩니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB