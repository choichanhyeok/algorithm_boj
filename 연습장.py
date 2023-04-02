


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



#
# str_a = input()
# str_b = input()
#
# count_a = [0] * 26
# count_b = [0] * 26
#
# pivot = ord('a')
#
# def count_alphabet(str_a, str_b):
#     for i in range(len(str_a)):
#         count_a[(ord(str_a[i]) - pivot)] += 1
#     for i in range(len(str_b)):
#         count_b[(ord(str_b[i]) - pivot)] += 1
#
#
# count_alphabet(str_a, str_b)
# answer = 0
#
# for cnt_a, cnt_b in zip(count_a, count_b):
#     answer += abs(cnt_a - cnt_b)
#
# print(answer)
# from typing import List
#
#
# def count_each_chr(str: str) -> List[int]:
#     str_cnt = [0] * 26
#     for chr in str:
#         str_cnt[ord(chr) - ord('A')] += 1
#     return str_cnt
#
#
# def get_max_idx(str_cnt: List[int]) -> int:
#     max_value = 0
#     max_idx = 0
#
#     for i in range(len(str_cnt)):
#         if str_cnt[i] > max_value:
#             max_value = str_cnt[i]
#             max_idx = i
#     if str_cnt.count(max_value) > 1:
#         return -9999
#     return max_idx
#
# str = input()
# str = str.upper()
#
# str_cnt = count_each_chr(str)
# max_idx = get_max_idx(str_cnt)
#
# if max_idx == -9999:
#     print('?')
# else:
#     print(chr(ord('A') + max_idx))






