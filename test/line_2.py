


# 문제 요약
# 당신은 유저 채팅을 분석, 비속어 단속 프로그램을 만들려고 합니다.
# 비속어 단어들을 담은 비속어 단어 사전이 있는데, 단어 사전을 참고해서 비속어를 사용한 유저 채팅을 단속하고자 한다.
# 유저 채팅은 알파벳 소문자 혹은 특수문자 점(.)으로 이루어진 단어들을 공백 하나로 구분한 문자열 형태입니다.
# 당신이 만든 프로그램은 다음과 같은 방법으로 비속어를 걸러내야합니다.


# 비속어 단어와 완벽히 일치하는 단어가 있으면, 단어 길이만큼의 특수문자(#)으로 대체합니다.
# 단어에 포함된 점(.)을 1 이상 k 이하 길이의 알파벳들로 대체했을 때 비속어 단어가 될 수 있으면 . 이 포함된
#

########################################################################################################################
# TODO: best_case. 빈도수 배열을 이용해, 문자열에서 최빈값을 가진 문자 찾기
def find_max_occurred_alphabet(string):
    '''
    입력받은 string의 문자 빈도수를 계산해, 최빈값을 구하는 함수
    :param string: 입력 string
    :return: 최빈값 문자 ex: 'a'
    '''

    ## step1. 빈도수 배열 만들어, 각 문자의 빈도수 저장하기
    alphabet_occurrence_array = [0] * 26                            # 빈도수를 넣을, 알파벳의 순서에 매핑된 배열 정의

    for alphabet in string:                                         # 입력받은 string의 문자 빈도수 계산
        if not alphabet.isalpha():                                  # 단, alphabet일 때
            continue # 반복문의 다음 인덱스로 넘어가
        alphabet_occurrence_array[ord(alphabet) - ord('a')] += 1    # 알파뱃의 index주소 추출 이후, 인덱스 배열의 해당 위치에 빈도수 값 +1


    #step2. 빈도수 배열 순회하며, 최빈값 비교. 최빈값의 index 주소 계속해서 update
    max_occurrence = 0              # 최다 빈도수 정보
    max_alphabet_index = 0          # 최다 빈도수가 담긴 문자의 주소

    for index in range(len(alphabet_occurrence_array)):             # alphabet_occurrence_array:  [1, 0, 3 .... 0] => 빈도수 배열
        alphabet_occurrence = alphabet_occurrence_array[index]      # 빈도수가 담긴 배열(max_occurrence) 순회,
        if max_occurrence < alphabet_occurrence:                    # 기존 max_occurrence보다 큰 경우,
            max_occurrence = alphabet_occurrence                    # 해당 index로 update
            max_alphabet_index = index
    return chr(ord("a") + max_alphabet_index)                       # a에서 해당 알파뱃의 위치 만큼의 index를 더해 최빈값 알파벳 출력


from typing import List

dic = ["slang", "badword"]
chat = "badword ab.cd bad.ord .word sl.. bad.word"


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''

    #TODO 1: chat을 split을 통해 단어별로 구성된 리스트로 만들어준다.
    chat_word_list = chat.split(' ')

    #TODO 2: 필터링 구분
    for word in chat_word_list:
        if word in dic:    # case1. 제외 단어랑 완전히 같을 때, *으로 대체한다
            answer += '*' * len(word)
        elif '.' in word:
            for exce in dic:
                if word[:2] in exce:
                    answer += '*' * len(word)
                    break







    return answer

print(solution(1, dic, chat))