#Q.  다음과 같은 문자열을 입력받았을 때, 각각의 문자의 빈도수중 가장 큰 값 찾기
# TODO: Q. 문자열에서 각각의 문자의 빈도수중 가장 큰 값 찾기
# KEY1:  char.isalpha() => 문자, 알파뱃 여부 식별
# KEY2: ord(char) => 아스키 코드값 리턴, 현재 알파벳 - 'a'의 아스키는 배열상 인덱스 추출의 결과 도출

########################################################################################################################
def find_alphabet_occurrence_array(string):
    '''
    입력 문자열 string문자열에서 각 문자의 빈도수중 가장 큰 수를 추출하는 메서드
    :param string:
    :return: 문자열에서 각 문자의 빈도수중 가장 큰 수
    '''
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if not alphabet.isalpha():                                      # 해당 문자가 알파벳이 아닐 때,
            continue                                                    # 반복문의 다음 인덱스로 넘어가

        alphabet_occurrence_array[ord(alphabet) - ord('a')] += 1        # 해당 알파벳에 index에 빈도수 1 추가
    return max(alphabet_occurrence_array)                               # 가장 높은 빈도수 추출 

# 복잡도: O(2*N)+1
########################################################################################################################

print(find_alphabet_occurrence_array("hello my name is sparta"))