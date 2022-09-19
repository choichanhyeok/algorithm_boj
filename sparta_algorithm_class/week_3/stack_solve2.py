def stack_sequence(n, sequence):

    result = []
    stack = []
    num = 1
    sequence_index = 0

    while True:
        if len(stack) == 0:
            stack.append(num)
            num +=1
            result.append("+")
        elif sequence[sequence_index] == stack[-1]:
            stack.pop()
            result.append("-")
            sequence_index += 1

            if len(stack) == 0:
                break

        else:
            if num > n:
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for target in result:
            print(target)



sequence = list()

n = int(input())
for _ in range(n):
    sequence.append(int(input()))

stack_sequence(n, sequence)