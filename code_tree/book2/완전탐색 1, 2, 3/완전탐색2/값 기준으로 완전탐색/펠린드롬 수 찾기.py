
x, y = tuple(map(int, input().split()))

answer = 0
for i in range(x, y+ 1):
    str_i = str(i)

    n = len(str_i)
    is_palindrome = True
    for j in range(n):
        if str_i[j] != str_i[-(j + 1)]:
            is_palindrome = False
            break
    if is_palindrome:
        answer += 1

print(answer)



#
# 두 개의 정수 X, Y가 주어지면 X이상 Y이하의 값 중 팰린드롬의 개수를 세려고합니다. 여기서 말하는 팰린드롬은 거꾸로 읽어도 제대로 읽는 것과 같은 수를 말합니다. 예를 들어 34543이나, 9009등이 팰린드롬에 해당하는 숫자입니다. 팰린드롬의 개수를 세는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 X와 Y가 공백을 사이에 두고 주어집니다.
#
# 10 ≤ X ≤ Y ≤ 1,000,000
# 출력 형식
# 첫 번째 줄에 팰린드롬의 개수를 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 98 132
# 출력:
#
# 5
# 예제 설명
# 98이상 132이하에 있는 팰린드롬의 수는 99, 101, 111, 121, 131로 총 5개 있습니다.