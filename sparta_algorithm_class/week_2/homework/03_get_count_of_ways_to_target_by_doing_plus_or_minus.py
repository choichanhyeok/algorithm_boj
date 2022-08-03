# Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
###########################################################################################################################################

numbers = [1, 1, 1, 1, 1]
target_number = 3
result_count = 0

#TODO. step1. 모든 합을 받아줄 리스트 정의
#TODO. step2. 모든 합을 순회하며 리스트를 채워준다.
#TODO. step3. 모든 합의 리스트들을 돌며 타겟 넘버를 채운 애들의 count를 기록해준다.
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    #종료 조건
    if len(array) == current_index:
        if current_sum == target:
            global result_count
            result_count += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index+1, current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - array[current_index])

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0))  # 5를 반환해야 합니다!
print(result_count)



########################################################################################################################
#
# numbers = [2, 3, 1]
# target_number = 0
# result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수
#
#
# def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
#     if current_index == len(array):  # 탈출조건!
#         if current_sum == target:
#             global result_count
#             result_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
#         return
#     get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
#                                                        current_sum + array[current_index])
#     get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
#                                                        current_sum - array[current_index])
#
#
# get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
# # current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
# print(result_count)  # 2가 반환됩니다!
#


###############################################################################################################################################
# Case2. 설명을 위한 형태1
# numbers = [2, 3, 1]
# target_number = 0
# result = []  # 모든 경우의 수를 담기 위한 배열
#
# # TODO: 재귀를 이용한 방법:
# def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
#     '''
#     각 경우의 수의 합들을 all_ways 배열에 넘겨준다.
#     :param array: 해당 함수를 호출한 곳에서 결과값 출력을 위해 넘겨준 포인터
#     :param current_index: 현재 주소, 순회와 종료 조건을 위해 필요
#     :param current_sum: 경우의 수의 합, all_ways에 append 해준다.
#     :param all_ways: 경우의 수들의 합을 담아둘 배열, 별도의 리턴 없이 포인터를 이용해 호출된 함수에서 바로 사용한다.
#     :return: -
#     '''
#     if current_index == len(array):
#         all_ways.append(current_sum)
#         print(current_sum)
#         return
#     get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], all_ways)
#     get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], all_ways)
#
#
# get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
# print(result)
# # current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
# # 모든 경우의 수가 출력됩니다!
# # [6, 4, 0, -2, 2, 0, -4, -6]