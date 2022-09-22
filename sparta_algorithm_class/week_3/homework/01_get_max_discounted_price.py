shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# 가격 리스트 정렬 (역순)
# 할인률 리스트 역순 정렬

# 할인률 적용 되는 애들만 합 구하기
# 적용 안되는 애들꺼 다 더하기



def get_max_discounted_price(prices, coupons):
    max_discount_price = 0
    prices.sort(reverse= True)
    prices_index = 0

    coupons.sort(reverse= True)
    coupons_index = 0

    #Todo: 할인률 적용 되는 애들만 합 구하기
    while prices_index < len(prices) and coupons_index < len(coupons):
        max_discount_price += prices[prices_index] * (100-coupons[coupons_index]) / 100

        coupons_index += 1
        prices_index += 1

    #TODO: 할인 쿠폰 없어서 그냥 적용해야 하는 애들 합 더해주기
    while prices_index != len(prices):
        max_discount_price += prices[prices_index]
        prices_index += 1

    return max_discount_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))