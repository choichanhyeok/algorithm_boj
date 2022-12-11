import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    max_heap = []
    last_added_index = 0
    answer = 0

    while stock < k:
        # 각 공급 날짜의 값들 중 최고 값 (heap을 이용)을 저장하다가, 공급 날짜까지 재고로 못 버티는 경우 stock를 공급 받아준다.
        while last_added_index < len(dates) and stock >= dates[last_added_index]:
            heapq.heappush(max_heap, -supplies[last_added_index])

            last_added_index += 1
        stock += -heapq.heappop(max_heap)
        answer += 1

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))