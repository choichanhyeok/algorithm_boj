from collections import deque

def solution(flowers):
    answer = 0
    flowers = deque(flowers)
    while flowers:
        flower = flowers.popleft()
        now_flower_born_date = int(flower[0])
        now_flower_dead_date = int(flower[1])
        try:
            next_flower_born_date = int(flowers[0][0])
        except:
            next_flower_born_date = 2100000000

            # quarter1. flowers[i+1][0](꽃이 피는 날짜)이 현재 flower의 지는 날짜와 겹칠 때
        if next_flower_born_date < now_flower_dead_date:
            answer += (now_flower_dead_date - now_flower_born_date) - (now_flower_dead_date - next_flower_born_date)

        else:  # quarter2. flowers[i+1][0](꽃이 피는 날짜)이 현재 flower의 지는 날짜와 겹치지 않을 때
            answer += (now_flower_dead_date - now_flower_born_date)

    return answer


print(solution([[2, 5], [3, 7], [10, 11]]))