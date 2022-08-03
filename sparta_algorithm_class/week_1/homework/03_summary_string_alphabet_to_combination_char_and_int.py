# Q.
# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.
# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.
########################################################################################################################
input_str = "acccdeee"
########################################################################################################################

# TODO: imagine(1-1).  알파뱃 빈도수 리스트를 만들어, string을 순회하며 나온 char에 대해 ord를 적용해, 해당 인덱스에 빈도수 추가
# TODO: imagine(1-2).  알파벳 빈도수 리스트 크기 만큼 for문을 돌며 해당 인덱스의 값과, chr(ord('a')+index)+빈도수리스트[index]를 통해 => ex. 'a8'와 같은 문자열을 도출해낸다
def summarize_string(input_str):
    alphabet_occurence_array = [0] * 26
    result_list = []
    #TODO: imagine(1-1): 알파벳 빈도수 리스트 구현
    for char in input_str:
        if not char.isalpha():
            continue
        alphabet_occurence_array[ord(char)-ord('a')] +=1

    #TODO: imagine(1-2): 빈도수 리스트를 보면서, 해당 알파벳과 빈도수 추출후 결과 리스트에 저장
    for index in range(len(alphabet_occurence_array)-1):
        result_list.append(chr(ord('a')+index)+str(alphabet_occurence_array[index]))

    return result_list
# 복잡도: O(2*N) => O(N)
########################################################################################################################
print(summarize_string(input_str))