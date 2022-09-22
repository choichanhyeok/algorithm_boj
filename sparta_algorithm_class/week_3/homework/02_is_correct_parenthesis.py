s = "(())()("



# 조건1: ')'가 있으면 '('가 있는지 확인한다
# 조건2: '('에 대한 정보를 다 저장한다.


def is_correct_parenthesis(string):
    stack = []

    for idx in range(len(string)):
        if string[idx] == '(':
            stack.append(idx)
        elif string[idx] == ')':
            try:
                stack.pop()
            except:
                return False

    if len(stack) != 0:
        return False
    else:
        return True



print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))

# def is_correct_parenthesis(string):
#     stack = []
#
#     for idx in range(len(string)):
#         if string[idx] == '(':
#             stack.append(idx)
#
#         elif string[idx] == ')':
#             try:
#                 stack.pop()
#             except:
#                 return False
#     if len(stack) != 0:
#         return False
#     else:
#         return True