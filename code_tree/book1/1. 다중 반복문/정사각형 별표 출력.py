# 정수 n의 값을 입력받아 별표로 정사각형을 출력하는 프로그램을 아래 예를 참고하여 작성해보세요.
#
# ex.
# 입력:
# 4
# 출력:
#
# ****
# ****
# ****
# ****

n = int(input())


for i in range(n):
    for j in range(n):
        print('*', end='')
    print()