# def stack_sequence(n, sequence):
#     count = 1
#     stack = []
#     result = []
#
#     for data in sequence:
#         while count <= data:
#             stack.append(count)
#             count += 1
#             result.append('+')
#         if stack[-1] == data:
#             stack.pop()
#             result.append('-')
#         else:
#             print(stack)
#             print("NO")
#             exit(0)
#     print('\n'.join(result))

















def stack_sequence(n, sequence):
    pivot = 1
    stack = []
    result = []

    while sequence:
        target = sequence.pop()

        # TODO 1. target까지 stack push
        while pivot <= target:
            stack.append(pivot)
            result.append('+')
            pivot += 1

        # TODO 2. target 내용 pop()
        if stack[-1] == target:
            result.append('-')
            stack.pop()

        # TODO 3. 그 밖의 경우 announce 'NO', then exit()
        else:
            print("No")
            exit(0)

    print('\n'.join(result))


sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)