from sys import stdin, stdout


def isvaild(str):
    stack = []

    for c in str:
        if c in "[(":
            stack.append(c)
        elif c == ")":
            if not stack or stack.pop() != '(':
                return False
        elif c == "]":
            if not stack or stack.pop() != '[':
                return False
    return not stack


while True:
    str = stdin.readline()
    if str == '.\n':
        break
    stdout.write("yes\n" if isvaild(str) else "no\n")

# from sys import stdin
#
# while True:
#     str_temp = stdin.readline().rstrip()
#     str = ''
#
#     if str_temp == '.':
#         break
#
#     for c in str_temp:
#         if c == '[' or c == ']' or c == '(' or c == ')':
#            str += c
#
#     while "()" in str or "[]" in str:
#         str = str.replace("()", '')
#         str = str.replace("[]", '')
#
#     if len(str) == 0:
#         print("yes")
#     else:
#         print("no")




# from sys import stdin
#
#
# while True:
#     str = stdin.readline()
#     if str[0] == '.' and len(str):
#         break
#
#     stack = []
#     stack2 = []
#     is_check = True
#
#     for c in str:
#         if c == '(':
#             stack.append(c)
#         elif c == ')':
#             if len(stack) == 0:
#                 is_check = False
#                 break
#             stack.pop()
#
#     for c in str:
#         if c == '[':
#             stack2.append(c)
#         elif c == ']':
#             if len(stack2) == 0:
#                 is_check = False
#                 break
#             stack2.pop()
#     if len(stack) != 0 or len(stack2) != 0:
#         is_check = False
#
#     if is_check:
#         print("YES")
#     else:
#         print("NO")
#
