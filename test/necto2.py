

def getMaximumRemovals(order, source, target):
    # print(order)
    # print(source)
    # print(target)

    count = 0
    succes = False
    for element in order:

        # TODO 1. 예외 처리를 위한 문자 찾기
        succes = True
        for except_char in target:
            if except_char in source:
                succes = False

        # TODO 2. 만약 예외처리할 문자가 없으면 count 리턴
        if succes == True:
            return count

        # TODO 3. source (ex. cdllekkw)에서 order에 기록된 인덱스를 살펴봐 target에 존재하는 문자가 있으면 _로 치환
        try:
            if source[element-1] in target:
                middle = target.index(source[element - 1])
                target = target[:middle - 1] + '*' + target[middle + 1:]
                source = source[:element - 1] + "_" + source[element + 1:]
            else:
                count += 1  # TODO 4. 치환할 일이 없으면 count +=1
        except:
            count += 1

    return count



order_count = int(input().strip())

order = []

for _ in range(order_count):
    order_item = int(input().strip())
    order.append(order_item)

source = input()

target = input()

result = getMaximumRemovals(order, source, target)
print(result)