# https://www.acmicpc.net/problem/21313



n = int(input())
# [1, 2]를 n//2(n을 2로 나눈 몫 만큼 곱하기) + 홀수이면 [3], 짝수이면 [] 더하기 ([3] if n%2 else [])
ans = [1, 2] * (n//2) + ([3] if n%2 else [])
print(*ans)

