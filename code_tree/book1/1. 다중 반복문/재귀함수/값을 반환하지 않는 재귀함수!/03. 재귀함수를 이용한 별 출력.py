#
# 1번째 N번째 줄까지 별 출력을 다음 모양으로 재귀함수를 이용해 출력하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 정수 N이 주어집니다.
#
# 1 ≤ n ≤ 100
# 출력 형식
# n개의 줄에 걸쳐 예제와 같이 별을 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 5
# 출력:
#
# *
# **
# ***
# ****
# *****


def print_star_triangle(n):
    if n == 0:
        return

    print_star_triangle(n - 1)
    print('*' * n)


n = int(input())

print_star_triangle(n)





