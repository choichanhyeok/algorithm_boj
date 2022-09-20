# https://school.programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    n = len(prices)
    result = []

    for i in range(n - 1):
        count = 0
        base_price = prices[i]
        for j in range(i, n - 1):
            if base_price > prices[j]:
                break
            count += 1
        result.append(count)
    result.append(0)
    return result