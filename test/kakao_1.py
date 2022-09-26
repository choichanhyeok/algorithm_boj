


# 고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다.
# 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다.

# 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다.
# 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.


# today = "2022.05.19"
today = "2020.01.01"
# terms = ["A 6", "B 12", "C 3"]
terms = ["Z 3", "D 5"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

day_pivot_dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8:31, 9:30, 10: 31, 11: 30, 12:31}

def date_to_array(today):
    date = list(map(int, today.split('.')))
    return date


def solution(today, terms, privacies):
    answer = []

    current_date = date_to_array(today)    # ['2022', '05', '19'] # 현재 날짜 배열로 저장
    privacie_date_list = [(privacie.split(' ')[0], privacie.split(' ')[1]) for privacie in privacies] # [('2021.05.02', 'A'), ('2021.07.01', 'B'), ('2022.02.19', 'C'), ('2022.02.20', 'C')]
    terms = {term.split(' ')[0]: int(term.split(' ')[1]) for term in terms}    # {'A': '6', 'B': '12', 'C': '3'} # term 정보 딕셔너리로

    date_num = 1
    for p_date, rank in privacie_date_list:
        p_date = list(map(int, p_date.split('.')))
        term = terms[rank]

        # case1. 현재 Month와 + term의 합이 12보다 클 때,
        if p_date[1] + term > 12:
            p_date[0] += 1
            p_date[1] = p_date[1] + term - 13

        else: # case2. 현재 Month와 + term의 합이 12보다 같거나 작을때,
            p_date[1] += term

        p_date[2] -= 1

        # case3. 일자가 0일 일 때,
        if p_date[2] == 0:
            p_date[2] = 28

        print(str(p_date) + '--')
        # print(current_date)
        for idx in range(len(p_date)):
            if p_date[idx] < current_date[idx]:
                # print(f'p_data[idx] = {p_date[idx]}, current_data[idx] = {current_date[idx]}')
                answer.append(date_num)
                break

        date_num += 1


    return answer

print(solution(today, terms, privacies))