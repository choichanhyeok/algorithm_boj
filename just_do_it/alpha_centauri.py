

nsclae = int(input())

for i in range(nsclae):
    current_index, target_index = map(int, input().split())
    count = 0

    # TODO 1: 광년 이동하면서 프로세스 진행 // 현재 위치와 목표 위치 같을때 종료
    while True:
        if current_index == target_index:
            print(count)
            break
        if current_index > target_index:
            print(count-1)
            break
        # TODO 2: k-1, k, k+1 광년 이동 => 무조건 k+1 광년이 이득이다.
        count += 1
        current_index += 1

    # TODO 3: k+1 광년이 목표 y보다 클 경우, count에 -1 => but !!!!!!!!!!
    #  1씩 올라가서 그럴 일 없음


    