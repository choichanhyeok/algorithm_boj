import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # (1) k일 이후에야 기존 공장이 정상 가동함
    # (2) 해외 공장에서 지급받을 수 있는데 이를 최소화 하고 싶음
    # (3) 해외 공장에서 밀가루 발주하는 날짜와 수량이 담긴 리스트를 이용해(dates, supplies)
    # (4) 최소 몇번 해외 공장에 컨택 해야 하는지 찾아내기

    # (5) stock(재고)가 k(재기동 날짜)와 같아질때까지 분석

    answer = 0
    max_heap = []
    date_index = 0

    while stock <= k:
        while date_index < len(dates) and dates[date_index] <= stock: # 각 모든 입고 날짜에 stock이 정상적으로 동작할 수 있는지,
                                                                      # 만약 그렇지 않다면 일단 아래 과정을 통해 stock 증가시키고 닷 ㅣ도전
            heapq.heappush(max_heap, -supplies[date_index])
            date_index += 1
        answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))