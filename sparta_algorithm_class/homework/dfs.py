# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)

    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)



# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#     visited_array.append(cur_node)
#     for adjacent_node in adjacent_graph[cur_node]:
#         if adjacent_node not in visited_array:
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)
# 각 cur_node의 인접 행렬을 뒤지면서, 해당 인접 노드가 방문 기록에 없으면 방문 기록에 추가해주는 dfs_recursion 실행, 이 경우 해당 노드의 인접 행렬도 다시 검사


# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#     visited_array.append(cur_node)
#
#     for adjacent_node in adjacent_graph[cur_node]:
#         if adjacent_node in visited_array:
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)



# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#     visited_array.append(cur_node)
#
#     for adjacent_node in adjacent_graph[cur_node]:
#         if adjacent_node not in visited_array:
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)

# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#     visited_array.append(cur_node)
#     for adjacent_node in adjacent_graph[cur_node]:
#         if adjacent_node not in visited_array:
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)

dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!