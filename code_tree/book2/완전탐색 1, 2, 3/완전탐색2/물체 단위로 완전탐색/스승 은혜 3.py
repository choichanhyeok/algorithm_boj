n, b = tuple(map(int, input().split()))
inputs = [  #  [[가격 A, 배송비 A], [가격 B, 배송비 B] ..]
    tuple(map(int, input().split()))
    for _ in range(n)
]

gift_cost = []


for i in range(n):
    price, delivery_cost = inputs[i]
    gift_cost.append((price, delivery_cost, (price)+delivery_cost))

gift_cost.sort(key = lambda x: (x[2]))
을
answer = 0
for i in range(n):
    sum_price = 0
    cnt = 0
    for j in range(n):
        price, delivery_cost, discount_cost = gift_cost[j]
        if i == j:
            sum_price += (price * 0.5) + delivery_cost
        else:
            sum_price += (price + delivery_cost)

        if b < sum_price:
            break
        cnt += 1

    answer = max(answer, cnt)

print(answer)



# 선생님이 N명의 학생에게 B만큼의 예산으로 선물을 주려고 합니다. 학생 i가 원하는 선물의 가격 P(i)와 배송비 S(i)가 있고, 선생님에게는 선물 하나를 정해서 반값으로 할인받을 수 있는 쿠폰이 있습니다. 선생님이 선물 가능한 학생의 최대 명수를 구하는 프로그램을 작성해보세요. 단, 선물의 가격은 항상 짝수입니다.
#
# 입력 형식
# 첫 번째 줄에 학생 수 N과 예산 B가 주어집니다.
#
# 두 번째 줄부터 각 줄마다 학생 N명이 원하는 선물의 가격 P(i)와 배송비 S(i)가 공백을 사이에 두고 주어집니다.
#
# 1 ≤ N ≤ 1,000
# 1 ≤ B ≤ 1,000
# 0 ≤ P(i), S(i) ≤ 1,000
# 출력 형식
# 첫 번째 줄에 선생님이 선물 가능한 학생의 최대 명수를 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 5 24
# 4 2
# 2 0
# 8 1
# 6 3
# 12 5
# 출력:
#
# 4
# 예제 설명
# 선생님이 만약에 3번 학생의 선물에 쿠폰을 쓴다면 1번 학생부터 4번 학생까지 선물해줄 수 있습니다. (4+2)+(2+0)+(4+1)+(6+3) = 22. 만약에 1번 학생이나 4번 학생의 선물에 쿠폰을 썼어도 여전히 1번부터 4번 학생까지 선물해 줄 수 있습니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB