# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

#조건1: 1과 자기 자신을 제외한 수로 나뉘어지지 않음  (mine%i != 0)
#조건2: n을 소수 prime으로 나눌 때, prime의 제곱은 n보다 크지 않다. (n<=prime)
########################################################################################################################

input = 1000000
########################################################################################################################
#TODO: 입력받은 정수(number) 이하의 소수를 모두 반환하는 메서드 정의
def find_prime_list_under_number(number):
    '''
    input으로 넘어논 number 까지의 소수 리스트를 리턴하는 메서드
    :param number:
    :return: number 까지의 소수 리스트
    '''
    prime_list = []

    # TODO: case1.2와 3의 합성수를 제외한 모든 것들은 소수이다. 소수에 2와 3이 포함되니, 소수 리스트를 순회하며 나누어 떨어지지 않는 것들만 prime_list에 추가하면 된다.
    ####################################################################################################################
    for i in range(2, number+1):
        for prime in prime_list:                      # 숫자가 엄청나게 커졌을 경우, prime*prime이 도움일 될 수 있음. 확실히
            if prime * prime <= i and i%prime == 0:   # => 소수가 아님을 판별, i에는 소수가 아닌 2~20까지 수가 다 들어감
                break
        else:
            prime_list.append(i)
    return prime_list
# 복잡도: O(N*M)
########################################################################################################################
result = find_prime_list_under_number(input)
# print(result)
