# 양의 정수를 원소로 갖는 길이가 N인 수열이 입력으로 주어졌을 때, 이 수열을 오름차순으로 정렬 했을 때 각각의 위치에 있던 원소가 어느 위치로 이동하는지 출력하는 코드를 작성해보세요.
#
# 입력 형식
# 첫째 줄에는 수열의 길이를 나타내는 양의 정수 N이 주어지고, 둘째 줄에는 N개의 양의 정수인 원소가 빈칸을 사이에 두고 주어집니다. 숫자가 중복되어 주어질 수 있습니다.
#
# 1 ≤ N ≤ 1,000
#
# 1 ≤ 수열의 원소 ≤ 1,000,000
#
# 출력 형식
# 이 수열을 정렬했을 때 각각의 위치에 있던 원소가 어느 위치로 이동하는지를 공백을 사이에 두고 출력하는 코드를 작성해보세요. 동일한 원소의 경우, 먼저 입력으로 주어진 원소가 더 앞으로 와야 합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 7
# 3 1 6 2 7 30 1
# 출력:
#
# 4 1 5 3 6 7 2


n = int(input())
arr = tuple(map(int, input().split()))


numbers = [
    (i, numb)
    for i, numb in enumerate(arr)
]

numbers.sort(key = lambda x: (x[1], x[0]))

index_list = [
    0 for _ in range(n)
]


for i, numb in enumerate(numbers):
    index_list[numb[0]] = i+1


for x in index_list:
    print(x, end = ' ')