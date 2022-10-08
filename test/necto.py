

def minNum(samDaily, kellyDaily, difference):

    # pre. Sam의 학습량에 differnece 만큼의 가중치 추가, kelly는 값 그대로 저장
    samSolved = samDaily + difference
    kellySolved = kellyDaily

    count = -1

    # except1. 애초에 kelly 학습량이 많은 경우
    if samSolved < kellyDaily:
        return 1

    # except2. 애초에 kelly가 학습할 의지가 없는 경우
    if difference == 0:
        return -1

    # TODO 1. 켈리의 학습량이 Sam에 도달할때 까지 count 증가
    while samSolved >= kellySolved:
        samSolved += samDaily
        kellySolved += kellyDaily

        count += 1

    # TODO 2. 켈리의 학습량이 애초에 sam보다 큰 경우
    if count != -1:
        count += 2

    return count


if __name__ == '__main__':
    samDaily = int(input().strip())
    kellyDaily = int(input().strip())
    difference = int(input().strip())

    result = minNum(samDaily, kellyDaily, difference)
    print(result)