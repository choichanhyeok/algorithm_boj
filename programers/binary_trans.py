<<<<<<< HEAD
# def solution(s):
#     answer = []

#     count_trans_binary = 0
#     count_trans_zero = 0


#     while True:
#         if s == '1':
#             break
#         count_trans_zero += s.count('0')
#         count_trans_binary += 1
#         c = len(s.replace('0', '')) # 이진 변환할 대상, c(길이)
#         binary_result = []

#         while c != 1:
#             if (0 == c % 2):
#                 binary_result.append('0')
#             else:
#                 binary_result.append('1')
#             c = c // 2

#         binary_result.append('1')
#         s = ''.join(binary_result)


#     return [count_trans_binary, count_trans_zero]


def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
=======
test
>>>>>>> cf402bd85b1099bd3b5011db6848d8c8565d380b
