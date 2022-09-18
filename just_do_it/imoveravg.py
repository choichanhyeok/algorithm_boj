# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# https://www.acmicpc.net/problem/4344


# 핵심 로직
# 1. 한 라인의 평균값 도출
# 2. 해당 라인에서 해당 평균값보다 높은 점수의 학생 비율 도출


nsize = int(input())

for i in range(nsize):
    scores = list(map(int, input().split()))

    # (1) 반 평균 구하는 로직
    nsum = sum(scores[1:])
    navg = nsum/scores[0]

    # (2) 평균보다 높은 비율 찾는 로직
    cnt = 0
    for j in range(1, scores[0]+1):
        if scores[j] > navg:
            cnt += 1
    print(f"{cnt/scores[0]*100:.3f}%")



