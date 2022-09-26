

# [문제 요약]
# 배열에 원소 추가하는 작업
# 배열의 크기는 배열이 생성될 때 결정되어 변하지 않습니다.  -> 그냥 배열에 대한 설명

# 원소를 추가했을 때 배열의 크기가 원소의 수보다 작다면,  len(arr) < len(add_element)
# 모든 원소를 담을 수 있는 더 큰 배열을 준비해서 기존 배열에 담긴 모든 원소를 새 배열로 복사한 후에  arr2(더 큰 배열) = arr
# 원소를 추가합니다.  arr2 + add_element

# 배열 번호와 해당 배열에 넣으려는 원소의 수를 담은 쿼리가 주어집니다.
# 쿼리를 모두 수행시, 원소가 복사된 횟수를 구하려고 한다.

# [조건]
# 원소를 추가하더라도 원소의 수가 배열의 크기보다 작거나 같다면, 기존 배열에 원소를 추가
# 원소를 추가하면 원소의 수가 배열의 크기보다 커지는 경우, 새로운 배열의 크기는 원소의 수 이상인 2의 거듭제곱 중에서 가장 작은 값
# 새로운 배열에 기존 배열의 모든 원소를 복사한 후에 원소를 추가 합니다. 배열의 번호는 바뀌지 않습니다.



# Q1. 현재 max_arr_size의 2의 거듭제곱중에 가장 작은 값을 매번 어떻게 구해주나? (모듈화)
# Q2. 배열 번호가 왜 필요해?  추가할 원소의 limit 값을 저장하기 위해서
# Q3.



queries = [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]
# queries = [[1, 1], [1, 2], [1, 4], [1, 8]]



#TODO 1: 배열 재생성시 arr_numbs_limit의 값 += 2^n 해주기

from typing import List

power_list = [2 ** n for n in range(1, 18)]     # 배열의 거듭 제곱


#TODO 2: 거듭 제곱을 찾음
def find_proper_power(element_size):
    proper_power = None

    for idx in range(len(power_list)):
        if power_list[idx] > element_size:
            proper_power = power_list[idx]
            break
    return proper_power


def solution(queries: List[List[int]]) -> int:
    arr_numbs = [0] * 100000
    arr_numbs_limit = [0] * 100000                  # 원소 추가시 변경되는 limit 값 확인

    answer = 0
    for idx in range(len(queries)):
        cur_arr_index = queries[idx][0]
        cur_arr_limit_size = arr_numbs_limit[cur_arr_index]
        cur_arr_size = arr_numbs[cur_arr_index]
        add_element_size = queries[idx][1]

        # TODO 2: queries의 배열 번호의 limit를 확인! 뭐랑 비교해? arr_numbs_limit[idx](현재 배열 번호의 길이)랑 len(queries[idx][1])(추가되는 원소 길이+기존 배열 길이) 비교
        # TODO 2-1: 현재 배열 번호의 길이가 0인 경우 -> 값의 복사가 이루어지지 않음  (answer을 증가시킬 이유가 없음), arr_numbs_limit와 arr_numbs 재정의
        if cur_arr_limit_size == 0:
            # print(f'add data: {add_element_size}')
            arr_numbs_limit[cur_arr_index] = find_proper_power(add_element_size)  # 해당 배열 번호의 limit 값 재정의
            arr_numbs[cur_arr_index] = cur_arr_limit_size + add_element_size            # 해당 번호의 배열에 현재 크기와, 추가되는 요소의 사이즈를 배열의 해당 번호에 저장

        # TODO 2-2: 현재 배열 번호의 길이가 1이상인 경우 ->  (1) limit > cur_arr_size + add_element_size,  (2) limit < cur_arr_size + add_element_size
        else: #(1)
            if arr_numbs_limit[cur_arr_index] >= cur_arr_size + add_element_size:
                arr_numbs[cur_arr_index] = cur_arr_size + add_element_size
            else:
                arr_numbs_limit[cur_arr_index] = find_proper_power(cur_arr_size + add_element_size)

                answer += cur_arr_size
                arr_numbs[cur_arr_index] = cur_arr_size + add_element_size

    return answer

print(solution(queries))