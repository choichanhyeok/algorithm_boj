
# 정수 n의 값을 입력받아 별표를 출력하는 프로그램을 아래 예를 참고하여 작성해보세요.
# n에 2를 입력받는 경우
#
# * * *
#   *
# n에 3을 입력받는 경우
#
# * * * * *
#   * * *
#     *

n = int(input())



for i in range(1, ( 2 *n ) +1, 2):
    for _ in range( i//2):
        print(' ', end = ' ')
    for _ in range(( 2 *n ) -i):
        print('*', end = ' ')
    print()
