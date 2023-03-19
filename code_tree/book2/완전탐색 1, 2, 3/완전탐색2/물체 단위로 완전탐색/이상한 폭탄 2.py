


def solution_a():
    n, k = map(int, input().split())  # 폭탄 개수와 거리 입력받기
    bombs = [int(input()) for _ in range(n)]  # 폭탄 번호 입력받기

    max_num = -1  # 가장 큰 번호 초기값 설정

    for i in range(n):
        cnt = 1  # 같은 번호를 가진 폭탄 개수
        for j in range(i+1, n):
            if bombs[i] == bombs[j] and j-i <= k:  # 같은 번호이고 거리가 K 이하인 경우
                cnt += 1  # 같은 번호를 가진 폭탄 개수 증가
        if cnt > 1:  # 같은 번호를 가진 폭탄이 2개 이상인 경우
            max_num = max(max_num, bombs[i])  # 가장 큰 번호 갱신

    if max_num == -1:  # 폭탄이 전혀 터지지 않은 경우
        print(max_num)
    else:
        print(max_num)  # 가장 큰 번호 출력


def solution_b():
    # (1) input: {n: 폭탄의 개수, k: 같은 번호상의 폭탄이 폭발하는 거리 조건}
    n, k = tuple(map(int, input().split()))
    bomb_numbers = [
        int(input())
        for _ in range(n)
    ]
    answer = -1

    # 같은 번호에 있는게 k번 안에 있는지 확인하면 된다.
    for i in range(n):
        for j in range(i + 1, n):
            if j - i > k:
                break

            if bomb_numbers[i] != bomb_numbers[j]:
                continue

            answer = max(answer, bomb_numbers[i])

    print(answer)




# 이상한 폭탄이 N개 있습니다. 이 이상한 폭탄은 각자에게 부여된 번호가 있고, 같은 번호가 부여된 폭탄끼리 거리가 K안에 있다면 폭발하게 됩니다. 폭탄의 개수 N, 특정 거리인 K, 그리고 폭탄을 나열한 순서가 주어지면, 폭발 할 폭탄중에 부여된 번호가 가장 큰 번호를 출력하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 N 과 K가 공백을 사이에 두고 주어집니다.
#
# 두 번째 줄부터 각 줄마다 폭탄의 순서가 주어집니다.
#
# 0 ≤ 폭탄의 번호 ≤ 1,000
# 1 ≤ N ≤ 100
# 1 ≤ K ≤ N
# 출력 형식
# 첫 번째 줄에 폭발 할 폭탄중에 번호가 가장 큰 번호를 출력합니다. 터지는 폭탄이 전혀 없다면 '-1'을 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 6 3
# 7
# 3
# 4
# 2
# 3
# 4
# 출력:
#
# 4
# 예제 설명
# 폭탄의 순서는 7, 3, 4, 2, 3, 4 입니다. 이때, 거리 3 이내에 있는 폭탄들은 전부 터지게 되므로 이 중 가장 큰 번호는 4번이 됩니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB