from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # bfs는 그냥 탐색 하는 알고리즘

    #TODO 1. 첫 방문한 인덱스의 visited[start]를 True로
    visited[start] = True
    #TODO 2. 탐색할 인접 행렬을 deque에 집어넣어
    queue = deque([start])

    #TODO 3. 그래프를 탐색하면서
    while queue:
      n = queue.popleft()
      print(n, end='')
      for cur_node_index in graph[n]:
        if not visited[cur_node_index]:
          visited[cur_node_index] = True
          queue.append(cur_node_index)




# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)