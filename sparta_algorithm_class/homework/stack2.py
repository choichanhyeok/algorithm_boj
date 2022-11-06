def stack_sequence(n, sequence):
    count = 1
    stack = []
    result = []

    for data in sequence:
        while count <= data:
            stack.append(count)
            count += 1
            result.append('+')
        if stack[-1] == data:
            stack.pop()
            result.append('-')
        else:
            print(stack)
            print("NO")
            exit(0)
    print('\n'.join(result))



sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)