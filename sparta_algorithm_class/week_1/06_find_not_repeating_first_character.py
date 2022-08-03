# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
#    만약 그런 문자가 없다면 _ 를 반환하시오.


input = "abadabac"
########################################################################################################################
def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26            #알파벳 빈도수 배열 정의

    #TODO: 알파뱃 빈도수 배열에 string의 빈도수 기록 => [alphabet_occurrence_array]
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char)-ord('a')
        alphabet_occurrence_array[arr_index] += 1

    #TODO: 빈도수 배열을 보며 반복되지 않은 알파벳(값이 1인) 추출  + in 속도를 위해 set으로 설정
    none_repeating_character_array = set()
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] == 1:
            none_repeating_character_array.add(chr(ord('a')+index))

    #TODO: none_repeating_character_array에서 뭐가 string의 첫번째 미반복 문자인지 모르니, string을 순회하며 비교
    for char in string:
        if char in none_repeating_character_array: # ** 내부적으로 해시를 사용하는 Set이 list보다 더 빠른 접근이 가능해 Set 사용
            return char

    return "_" # none_repeating_character_array에서 미반복 문자가 나오지 않았을 시 _을 리턴

# 시간 복잡도:  O(N) + O(N) + O(N) = O(3N) = O(N)
########################################################################################################################

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))


# Key1: 알파벳 빈도수 배열 사용
# Key2: List대신 Set을 이용해 in 속도 O(N) => O(1)로 개선
# Key3: chr을 이용해 ord값을 문자로 형변환