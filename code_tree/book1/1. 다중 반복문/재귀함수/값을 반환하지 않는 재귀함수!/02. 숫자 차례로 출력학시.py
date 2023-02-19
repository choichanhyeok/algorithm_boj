# 정수 N이 주어지면 재귀함수를 2개 작성하여 첫 번째 재귀함수를 이용하여 1부터 N까지 숫자를 차례대로 출력하고, 두 번째 재귀함수를 이용하여 N부터 1까지 차례로 출력하는 프로그램을 작성해보세요. 단, 두 재귀함수 모두 인자로 N을 넘기는 함수여야만 합니다.
#
# 입력 형식
# 첫 번째 줄에 정수 N이 주어집니다.
#
# 1 ≤ N ≤ 100
# 출력 형식
# 첫 번째 줄에는 1부터 N까지 차례로 공백을 사이에 두고 출력합니다.
# 두 번째 줄에는 N부터 1까지 차례로 공백을 사이에 두고 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 7
# 출력:
#
# 1 2 3 4 5 6 7
# 7 6 5 4 3 2 1
# 제한


def print_to_N(n):
    if n == 0:
        return
    print_to_N(n-1)
    print(n, end = ' ')

def print_to_1(n):
    if n == 0:
        return
    print(n, end = ' ')
    print_to_1(n-1)

n = int(input())

print_to_N(n)
print()
print_to_1(n)
