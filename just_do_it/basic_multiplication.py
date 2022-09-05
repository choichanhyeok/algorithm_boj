#  https://www.acmicpc.net/problem/2588

a = int(input())
b = str(input())[::-1]

nsum = 0
i = 1
for target in b:
    print(a * int(target))
    nsum += a * int(target)*i
    i *= 10

print(nsum)