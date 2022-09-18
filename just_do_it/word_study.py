# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# https://www.acmicpc.net/problem/1157


words = input().upper()

# TODO 1: 각 숫자 개수 추출하기
unique_words = list(set(words))
cnt = []

for unique_word in unique_words:
    cnt.append(words.count(unique_word))

# TODO 2: 최대 개수의 숫자 출력 (예외: 최대 개수의 알파벳 2개 이상일 경우 "?" 출력)

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(unique_words[cnt.index(max(cnt))])