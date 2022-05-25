

# 다장조는 c:1, d:2, e:3, f:4, g:5, a:6, b:7, c:8
# 상태는 ascending, descending, mixed가 있다.
# 오름차순일 때(ascending), 내림차순일 떄(descending), 그 외(mixed)로 나눈다.

# 조건: 앞에 || 뒤에 요소와 비교를 통해 상태값 체크만 해주면 됌

ascending = True
descending = True


input_scale = list(map(int, input().split(' ')))

for i in range(1, len(input_scale)):
    pivot = input_scale[i]
    target = input_scale[i-1]
    if pivot > target:
        descending = False
    elif pivot < target:
        ascending = False
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')