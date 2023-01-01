# https://school.programmers.co.kr/learn/courses/30/lessons/12980

# def solution(n):
#     ans = 1

#     while n != 1:
#         if n % 2 != 0:
#             ans += 1
#         n = n // 2

#     return ans


def solution(N):
    return bin(N).count('1')