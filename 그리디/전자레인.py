
t = int(input())
a = b = c = 0
result_list = []


if t%10 != 0: # 최소 단위로 나누었을 때 0이 아니면 구할 수 없는 값
    print(-1)

else:
    a = t // 300
    b = (t%300)//60
    c = ((t%300)%60)//10
    print (a, b, c)