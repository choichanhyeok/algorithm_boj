# 정수 N이 주어지면 재귀함수를 이용해서 문자열 "HelloWorld"를 N번 출력하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 정수 N이 주어집니다.
#
# 1 ≤ N ≤ 20
# 출력 형식
# 첫 번째 줄부터 각 줄마다 문자열 "HelloWorld"를 총 N번 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 4
# 출력:
#
# HelloWorld
# HelloWorld
# HelloWorld
# HelloWorld



def print_hworld(n):
    if n == 0:
        return
    print_hworld(n-1) # end
    print('HelloWorld')

n = int(input())

print_hworld(n)