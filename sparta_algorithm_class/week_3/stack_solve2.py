def stack_sequence(n, sequence):
    result = []
    stack = []
    num = 1
    sequence_index = 0

    while True: # stack을 1부터 오름 차순으로 증가시키면서, 현재 sequence_index의 값과 같은놈 나오면 stack.pop()
        #TODO 1: 첫 시작시 stack에 1 추가
        if len(stack) == 0:
            stack.append(num)
            num += 1
            result.append('+')

        #TODO 2: 현재 stack의 head와 sequence_index의 값이 같은 경우 pop
        elif sequence[sequence_index] == stack[-1]:
            stack.pop()
            result.append('-')
            sequence_index += 1

            if len(stack) == 0:
                break

        #TODO 3: 그렇지 않은 경우 그냥 num 증가, stack에 push
        else:
            if num > n:
                print('no')
                break
            stack.append(num)
            result.append('+')
            num += 1

    if len(stack) == 0:
        for target in result:
            print(target)

sequence = list()

n = int(input())
for _ in range(n):
    sequence.append(int(input()))

stack_sequence(n, sequence)