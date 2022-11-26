from collections import deque

def solution(id_list, k):
    answer = 0
    issued_number = 1
    id_list = deque(id_list)
    coupon_issuance_count_dict = {}

    while id_list:
        today_id_list = id_list.popleft().split(' ')
        today_duplication_check_dict = {}
        for id in today_id_list:
            if today_duplication_check_dict.get(id):
                continue

            today_duplication_check_dict[id] = True
            if id not in coupon_issuance_count_dict:
                coupon_issuance_count_dict[id] = issued_number
            else:
                coupon_issuance_count_dict[id] += issued_number

    for target in coupon_issuance_count_dict.values():
        if target > k:
            answer += target - (target- k)
        else:
            answer += target

    return answer


print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))