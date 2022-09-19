# https://www.acmicpc.net/problem/10773




n = int(input())
stack = []

for i in range(n):
    #TODO 1: stack에 값을 받아서 0인지 확인한다. 0이라면 POP
    numb = int(input())
    if numb == 0:
        try:
            stack.pop()
        except:
            print('첫 요청을 0을 집어넣으면 pop()을할 수 없습니다.')
    else:
        stack.append(numb)

    ## 맨 처음 수가 0인거는 어떻게 처리해?
    
    
#TODO 2: 최종적으로 stack을 순회하며 합을 구한다
nsum = 0
for target in stack:
    nsum += target
print(nsum)




