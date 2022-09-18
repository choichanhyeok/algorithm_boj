
from collections import deque

queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

layer = [["XXXXX", "OOSXO", "OOXOO"], ["XEOOO", "OXXXO", "OOOOX"]]

layer_max = len(layer)

start_layer = ""
start_index = []
end_layer = ""

#TODO 1: 시작하는 레이어의 인덱스 도출 (층은 70개 이하기 때문에 O(N^2)이어도 문제 없음)
for i in range(len(layer)):                           # [["XXXXX", "OOSXO", "OOXOO"], ["XEOOO", "OXXXO", "OOOOX"]]: ["XXXXX", "OOSXO", "OOXOO"] -> ["XEOOO", "OXXXO", "OOOOX"]
    k = 0
    for target in layer[i]:                           # ["XEOOO", "OXXXO", "OOOOX"]: "XEOOO" -> "OXXXO" -> "OOOOX"
        if "S" in target:                             # detected "OOSXO" !!
            start_layer = i                           # start_layer = 'OOSXO'를 포함한 layer의 index => 0
            start_low = k                             # start_low = 'OOSXO'를 포함한 문자열의 index => 1
            start_index = target.index("S")           # start_index = 'OOSXO' 문자열에서 S의 index => 2
            queue.append(start_layer, start_low, start_index)  # queue에 시작 좌표 설정
        elif "E" in target:
            end_layer = i
        k += 1

# print(layer[start_layer][start_low][start_index]) # S값 도출 확인

#위 아래 탐색



# bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while queue:
        x, y, z = queue.popleft()           # 처음 시작 좌표를 x, y, z에 꺼내고
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z
            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
            if 0 <= nx < n and 0 <= ny < m and layer[nx][ny] == 'O':
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])




#TODO 2: 완전 탐색

# while True:
current_layer = start_layer
current_low = start_low
current_index = start_index


# for문 하나 더 ~
# 좌우 탐색
if layer[current_layer][current_low][current_index -1] == 'O':
    current_index = current_index-1

if layer[current_layer][current_low][current_index+1] == 'O':
    current_index = current_index+1

if layer[current_layer][current_low-1][current_index] == 'O':
    current_low = current_low-1

if layer[current_layer][current_low+1][current_index] == 'O':
    current_low = current_low+1

if layer[current_layer-1][current_low][current_index] == 'O':
    current_layer = current_layer-1

if layer[current_layer+1][current_low][current_index] == 'O':
    current_layer = current_layer-1



#     #탈출 조건(1): 모든 경우를 다 탐색한 경우


# 가짜 큐브 생성,
# 가짜 큐브에서 움직인 이후, 지나온 길은 close로 만들어줘
# 가짜 큐브에서 해당 인덱스 기준으로 6방향 체크
# 맨 처음 기준으로 몇번 움직였는지 체크, min_coast로 변경

# 탈출 조건(1): 
# 탈출 조건(2): 6방향 모두 close인 경우(이미 온 길 포함): -1 리턴

