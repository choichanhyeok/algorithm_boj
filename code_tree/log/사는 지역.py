#
# 이름, 번지수, 지역에 대한 n명의 자료가 주어지면, 사전순으로 이름이 가장 느린 사람의 자료를 출력하는 프로그램을 작성해보세요.
# 단, c언어의 경우 구조체를, 다른 언어의 경우 class를 이용하여 각 사람의 정보를 담은 객체 n개 만들어 문제를 해결해주세요.
#
# 입력 형식
# 첫 번째 줄에는 n이 주어집니다.
# 두 번째 줄 부터는 n개의 줄에 걸쳐서 각 줄마다
# 알파벳 소문자로 이루어진 이름, XXX-XXX(X는 숫자입니다)의 형태인 번지수, 그리고 지역이 공백을 사이에 두고 주어집니다.
# 같은 이름이 주어지는 경우는 없다고 가정해도 좋습니다.
#
# 1 ≤ n ≤ 10
# 1 ≤ 이름, 지역의 길이 ≤ 10

# 입출력 예제
# 예제1
# 입력:
#
# 3
# kim 987-123 Seoul
# lee 888-345 Busan
# park 743-866 Daegu
# 출력:
#
# name park
# addr 743-886
# city Daegu

class Address:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Address(name, address, region) for name, address, region in arr]

target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i

# 결과 출력
print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].address}")
print(f"city {people[target_idx].region}")