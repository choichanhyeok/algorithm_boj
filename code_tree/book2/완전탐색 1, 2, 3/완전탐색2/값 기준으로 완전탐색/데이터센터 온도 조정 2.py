MAX_TEMPERATURE = 1000 + 1

n, c, g, h = tuple(map(int, input().split()))
temperature_range = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = 0
for now_temperature in range(MAX_TEMPERATURE):
    workload = 0
    for i in range(n):
        min_temperature, max_temperature = temperature_range[i]

        # 온도에 따라
        if now_temperature < min_temperature:
            workload += c
        elif min_temperature <= now_temperature and now_temperature <= max_temperature:
            workload += g
        else:
            workload += h
    answer = max(answer, workload)

print(answer)




# 데이터센터 안에 있는 장비들의 효율을 위해 온도를 맞춰주려고 합니다. 각 장비들마다 선호하는 온도의 범위들이 전부 다릅니다. 각 장비의 작업량은 다음과 같이 정의됩니다.
#
# 만약 데이터센터의 온도범위가 장비 A가 선호하는 온도 Ta 보다 낮다면 C만큼의 작업량을 수행하고,
# 만약 데이터센터의 온도범위가 장비 A가 선호하는 온도 Ta이상 Tb 이하에 있다면 G만큼의 작업량을 수행하고,
# 만약 데이터센터의 온도범위가 장비 A가 선호하는 온도 Tb 보다 높다면 H만큼의 작업량을 수행합니다.
# 장비의 개수 N과 온도에 따른 장비들의 작업량 C, G, H가 주어지고 N개 장비들이 선호하는 온도의 범위가 주어지면 온도를 적절히 설정하여 데이터센터안의 최고 작업량을 출력하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 차례로 N, C, G, H가 공백을 사이에 두고 주어집니다.
#
# 두 번째 줄부터 N줄에 걸쳐 한 줄 하나씩 온도 범위 Ta, Tb가 공백을 사이에 두고 주어집니다.
#
# 1 ≤ N ≤ 1,000
# 0 ≤ Ta ≤ Tb ≤ 1,000
# 0 ≤ C, H ≤ G ≤ 1,000
# 출력 형식
# 첫 번째 줄에 데이터센터안의 최고 작업량을 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 4 7 9 6
# 5 8
# 3 4
# 13 20
# 7 10
# 출력:
#
# 31
# 예제 설명
# 온도가 7도나 8도인 경우, 첫 번째와 네 번째 장비는 G(=9)만큼 작업량을 뽑아낼 수 있고, 두 번째 장비는 H(=6), 세 번째 장비는 C(=7)를 뽑아낼 수 있습니다. 총 31의 작업량으로 이것이 최대로 뽑아낼 수 있는 작업량입니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
