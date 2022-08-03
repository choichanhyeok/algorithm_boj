

input = "abcba"
########################################################################################################################
def is_palindrome(string):
    '''
    재귀함수를 이용한 팰린드롬 판별
    :param string: 팰린드롬 여부를 판별한 문자열
    :return: 인풋이 팰린드롬인지 아닌지 여부
    '''
    if string <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

########################################################################################################################
# def is_palindrome(string):
#     '''
#     for문을 이용한 팰린드롬 판별
#     :param string: 팰린드롬 여부를 판별한 문자열
#     :return: 인풋이 팰린드롬인지 아닌지 여부
#     '''
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n-1-i]:
#             return False
#     return True
########################################################################################################################
print(is_palindrome(input))