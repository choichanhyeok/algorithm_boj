# 정수 n이 주어졌을 때, 아래 예를 참고하여 * 로 이루어진 직각삼각형 대칭으로 2 개 출력하는 프로그램을 작성해보세요.
#
# 예) n = 3 일 때
#
# ******
# **  **
# *    *
#
# 4
# 출력:
#
# ********
# ***  ***
# **    **
# *      *
#




n = int(input())

for i in range(n):
    for _ in range(n - i, 0, -1):
        print('*', end='')

    for _ in range(i * 2):
        print(end=' ')

    for _ in range(n - i, 0, -1):
        print('*', end='')

    print()