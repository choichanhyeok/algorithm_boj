#Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
# TODO: Q. 문자열에서 최빈값을 가진 문자 찾기

input = "hello my name is sparta"
result = [0]*26

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

# 시간 복잡도: O((N*2)+(N*2)) => O(N)
# ########################################################################################################################
# # TODO: case2. 완전 탐색을 이용해, 문자열에서 최빈값을 가진 문자 찾기
# def find_max_occurred_alphabet(string):
#     '''
#     입력받은 string의 각 문자중 최빈값을 가진 문자를 추출하는 메서드
#     :param string: 입력 string
#     :return: 최빈값을 가진 문자 ex: 'a'
#     '''
#     alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
#                       "t", "u", "v", "x", "y", "z"]
#
#     max_occurrence = 0                  # 최빈 값 비교를 위한 변수
#     max_alphabet = alphabet_array[0]    # 최빈 값 알파벳을 넣을 변수
#
#     for alphabet in alphabet_array:     # 1. a-z까지 알파벳을 모두 순회하면서
#         occurrence = 0
#         for char in string:             # 2. 입력받은 string에 하나씩 비교하며
#             if char == alphabet:        # 3. 같은 문자가 있는지 검사
#                 occurrence += 1         # 4. 같은 문자가 있을 시 빈도수 +1을 해주고,
#
#         if occurrence > max_occurrence: # 5. 최대 빈도수보다, 빈도수가 높으면
#             max_alphabet = alphabet     # 6. 최빈 알파벳을 업데이트 해준다.
#             max_occurrence = occurrence # 7. 비교를 위한 최빈값도 같이 업데이트
#
#     return max_alphabet
# # 시간 복잡도: O((N*1)*(N*2)) => O(N^2)
# ########################################################################################################################

result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))