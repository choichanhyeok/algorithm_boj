
# JOI 상점가에서는 포인트 카드 서비스를 실시하고 있다. 각 포인트 카드에는 도장을 찍을 수 있는 칸이 총 2N개 있어, 상품을 구매하면 뽑기를
# 해서 결과에 따라 '당첨' 또는 '꽝' 도장이 찍힌다. 한 칸에 두 번 이상 도장을 찍을 수는 없다. 2N개 중 N개 이상의 칸에 당첨 도장이 찍힌
# 포인트 카드는 경품과 교환할 수 있다. 또, 한 칸에 찍힌 도장을 1엔을 내고 다른 도장으로 바꿀 수 있다.
# JOI 군은 2N개 칸을 다 채운 포인트 카드를 M장 가지고 있다. i번째 포인트 카드에는 Ai개의 당첨 도장과, Bi개의 꽝 도장이 찍혀 있다.
# JOI 군은 M-1개 이상의 경품을 가지려고 한다. 이에 필요한 비용의 최솟값을 구하라.


# 각 포인트 카드에는 도장을 찍을 수 있는 칸이 총 2N개 있다.
# 상품을 구매하면 뽑기해서 결과에 따라 당첨, 꽝 도장 찍힘


n = int(input())
cost_list = list(map(int, input().split()))

max = cost_list[0]
nsum = cost_list[0]
for i in range(1, n):
    nsum += cost_list[i]
    if max < cost_list[i]:
        max = cost_list[i]

print(nsum-max)




