def solution_a(): # 적은 연산
    # (1) input {k: 경기의 수, n: 개발자의 수}
    k, n = map(int, input().split())

    # (2) rank: [[개발자A의 ID, 개발자 B의 ID .. n], [개발자A의 ID, 개발자 B의 ID .. n], .. k]
    rank = [
        [0] * n
        for _ in range(n)
    ]

    # 각 사람이 몇 번째 사람을 이겼는지에 대해 기록하면 된다. (전 경기 다 이겼으면 된 것)
    for _ in range(k):
        match_result = list(map(int, input().split()))

        for i in range(n):
            for j in range(i + 1, n):
                rank[match_result[i] - 1][match_result[j] - 1] += 1

    answer = 0
    for i in range(n):
        for j in range(n):
            if rank[i][j] == k:
                answer += 1

    print(answer)

def solution_b(): # 진짜 완전탐색 그 자체
    k, n = tuple(map(int, input().split()))

    match_history = [  # index: 유저 순위, value: 유저 id
        list(map(int, input().split()))
        for _ in range(k)
    ]

    answer = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue

            all_win = True
            for result in match_history:
                dev_idx_i = result.index(i)
                dev_idx_j = result.index(j)

                if dev_idx_j < dev_idx_i:
                    all_win = False

            if all_win:
                answer += 1

    print(answer)



# 개발자의 순위

# K번의 경기에 대해 N명의 개발자의 순위가 주어졌을 때, 항상 a번 개발자가 b번 개발자보다 더 높은 순위였던 서로 다른 (a, b) 쌍의 수를 구하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에는 K와 N이 공백을 사이에 두고 주어집니다.
#
# 두 번째 줄부터는 K개의 줄에 걸쳐 각 경기에 대한 결과인 N개의 정수값이 공백을 사이에 두고 주어집니다. 이 숫자는 각각의 개발자 번호를 의미하며, 먼저 입력으로 주어진 개발자의 순위가 더 높았음을 의미합니다. 한 경기에 대해 1부터 N까지의 숫자가 겹치지 않고 주어짐을 가정해도 좋습니다.
#
# 1 ≤ K ≤ 10
# 1 ≤ N ≤ 20
# 출력 형식
# 첫 번째 줄에는 불변의 순위에 대해 서로 다른 (a, b) 쌍의 수를 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 3 4
# 4 1 2 3
# 4 1 3 2
# 4 2 1 3
# 출력:
#
# 4
# 예제 설명
# 다음 4개의 쌍이 존재합니다.

# (4, 1) - 4번 개발자는 3번의 경기에 있어 1번 개발자보다 항상 순위가 높았습니다.
# (4, 2) - 4번 개발자는 3번의 경기에 있어 2번 개발자보다 항상 순위가 높았습니다.
# (4, 3) - 4번 개발자는 3번의 경기에 있어 3번 개발자보다 항상 순위가 높았습니다.
# (1, 3) - 1번 개발자는 3번의 경기에 있어 3번 개발자보다 항상 순위가 높았습니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB