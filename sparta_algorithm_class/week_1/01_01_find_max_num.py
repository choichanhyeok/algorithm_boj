
#Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
# TODO: Q. 최대값 찾기
input = [3, 5, 6, 1, 2, 4]

########################################################################################################################
#TODO: best_case. set을 통해 정렬 이후, 마지막 인덱스[-1] 값 조회를 통해 최대값 리턴
def find_max_num(array):
    '''
    입력된 array의 최대값을 리턴하는 메서드, set(집합)의 속성을 이용해 문제를 해결함.
    :param array: 숫자로 이루어진 배열 입력값
    :return: 인풋 array의 최대값
    '''
    target = set(array)    # => O(N)
    target = list(target)  # => O(N)
    return target[-1]

# 복잡도: O(2*N)
########################################################################################################################
# #TODO: case1. 배열의 첫번째 원소를 max_value에 넣어, 값 비교,
#
# def find_max_num(array):
#     '''
#     입력된 array의 최대값을 리턴하는 메서드, 탐욕적 속성을 이용해 문제를 해결함
#     :param array: 숫자로 이루어진 배열 입력값
#     :return: 인풋 array의 최대값
#     '''
#     max_value = array[0]
#     for num in array:    # O(N)
#         if num > max_value:   # + 1
#             max_value = num   # + 1
#     return max_value            # => O(2*N) + 1

# 복잡도: O(N)
########################################################################################################################
#TODO: case2. 2중 for문을 이용해 완전탐색한다.
#
# 이중 for문을 이용한 완전탐색 예제
# max_value = 0
# def find_max_num(array):
#     '''
#     입력된 array의 최대값을 리턴하는 메서드, 완전탐색을 이용해 문제를 해결함
#     :param array: 숫자로 이루어진 배열 입력값
#     :return: 인풋 array의 최대값
#     '''
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break
#         else: # for문이 다 돌 때 까지 break가 실행되지 않았다 => num보다 큰 숫자가 없었다
#             return num
# 복잡도: O(N^2)
########################################################################################################################
result = find_max_num(input)
print(result)