from sys import stdin, stdout

def is_correct_parenthesis(string):
    stack = []

    for c in string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False

    return not stack if "Yes" else "No"

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))


# from sys import stdin
#
# n = int(input())
# for _ in range(n):
#     str_ = stdin.readline().strip()
#     stack = 0
#     for chr_ in str_:
#         if chr_ == '(':
#             stack += 1
#         else:
#             stack -= 1
#             if stack < 0:
#                 break
#     if stack == 0:
#         print('YES')
#     else:
#         print('NO')