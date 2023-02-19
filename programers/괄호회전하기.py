# https://school.programmers.co.kr/learn/courses/30/lessons/76502


# 문제 설명
# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
#
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.


def solution(s):
    answer = 0
    bucket_mapping = {')': '(', '}': '{', ']': '['}
    # TODO 1. while로 문자열 s를 왼쪽으로 shift
    # TODO 2. 단, s의 초기 값과 같아지는 경우 break
    #           + origin_s
    # TODO 3. stack을 이용해서 ')', '}', ']'이 등장하는 경우에 pop()
    # TODO 4. 단, 각 괄호가 맵핑되지 않으면 answer에 여태껏 left shift한 횟수를 저장
    #           + 그럼 left shift를 저장할 변수가 필요하겠네? 변수명은 left_shift_count 괜찮을까?

    origin_s = s

    while True:
        temp = s
        stack = []
        is_correct = True

        for x in temp:
            if len(stack) != 0 and (x == ')' or x == ']' or x == '}'):
                bucket = stack.pop()
                if bucket_mapping[x] != bucket:
                    is_correct = False
            else:
                stack.append(x)

        if stack:
            is_correct = False

        s = s[1:] + s[0]  ## 왼쪽으로 한 칸 shift
        answer += (1 if is_correct else 0)
        if s == origin_s:
            break
    return answer