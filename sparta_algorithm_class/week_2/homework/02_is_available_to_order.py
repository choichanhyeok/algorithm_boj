shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# case2. 집합을 이용한 풀이 (개선안)
def is_available_to_order(menus, orders):
    """
    주문 요청(orders)을 하나하나 확인 (for)하면서, 해당 주문이(order)가 메뉴(menus_set)에 포함되어 있는지 확인하는 메서드
    :param menus: 가용 메뉴들이 담긴 리스트
    :param orders: 요청받은 주문 리스트
    :return:
    """

    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True
    # 그냥 list를 사용하지 않고, set을 사용하는 이유는 파이썬 내부적으로 list에 대한 탐색은 O(n), 집합에 대한 탐색은 O(1)이기 떄문이다.


# def is_available_to_order(menus, orders):  #case1. 이진 탐색을 이용한 풀이 (비개선안)
#     menus.sort()  # menus 정렬!
#     for order in orders:
#         if not is_existing_target_number_binary(order, menus): #해당 주문이 menus에 있는지 판별
#             return False
#     return True
# 
# 
# def is_existing_target_number_binary(target, array):
#     current_min = 0
#     current_max = len(array) - 1
#     current_guess = (current_min + current_max) // 2
# 
#     while current_min <= current_max:
#         if array[current_guess] == target:
#             return True
#         elif array[current_guess] < target:
#             current_min = current_guess + 1
#         else:
#             current_max = current_guess - 1
#         current_guess = (current_min + current_max) // 2
# 
#     return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)