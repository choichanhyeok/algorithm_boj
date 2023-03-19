# 변수 선언 및 입력
x, y = tuple(map(int, input().split()))

ans = 0

# 각 숫자에 대해
# 흥미로운 숫자인지 아닌지 여부를 판단합니다.
for i in range(x, y + 1):
	num = i
	digit = [0] * 10
	all_digit = 0

	while num:
		digit[num % 10] += 1
		all_digit += 1
		num //= 10

	is_interesting_numb = False

	for j in range(10):
		if digit[j] == all_digit-1:
			is_interesting_numb = True
	if is_interesting_numb:
		ans += 1
print(ans)



# 두 개의 숫자 X, Y가 주어지면 X이상 Y이하에 있는 ‘흥미로운 숫자’의 개수를 세려고합니다. 여기서 말하는 ‘흥미로운 숫자’란 모든 자릿수에 있는 숫자들이 같지만, 정확히 한 자리만 다른 숫자를 의미합니다. 예를 들어 33335와 1118은 정확히 한 자리만 다르므로 ‘흥미로운 숫자’지만, 333333는 전부 같은 숫자로만 이루어져 있고 11188은 정확히 한 자리만 다른 것은 아니므로 ‘흥미로운 숫자’가 아닙니다. ‘흥미로운 숫자’의 개수를 세는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 X와 Y가 공백을 사이에 두고 주어집니다.
#
# 100 ≤ X ≤ Y ≤ 1,000,000
# 출력 형식
# 첫 번째 줄에 흥미로운 숫자의 개수를 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 110 133
# 출력:
#
# 13
# 예제 설명
# 110이상 133이하에 있는 흥미로운 숫자들은 110, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 131, 133로 총 13개가 있습니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB