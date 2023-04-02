


# a = ['2', '4', '6', '8', '5', '7']
# b = ['4', '6', '8']
#
# a = ''.join(a)
# b = ''.join(b)
#
# print(a)
# print(b)
# print('Yes' if b in a else 'No')


# s = input()
# standard = ord('a')
#
#
# for c in s:
#     if ord(c) < standard:
#         print(c.lower(), end = '')
#     else:
#         print(c.upper(), end = '')




str_a = input()
str_b = input()

count_a = [0] * 26
count_b = [0] * 26
pivot = ord('a')


for i in range(len(str_a)):
    count_a[(ord(str_a[i]) - pivot)] += 1
for i in range(len(str_b)):
    count_b[(ord(str_b[i]) - pivot)] += 1

answer = 0
for cnt_a, cnt_b in zip(count_a, count_b):
    answer += abs(cnt_a - cnt_b)

print(answer)


