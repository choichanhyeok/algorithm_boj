def solution(s):
    array = list(map(int, s.split(' ')))
    return str(min(array)) + ' ' + str(max(array))

# import heapq

# def solution(s):
#     max_queue = []
#     min_queue = []

#     s = list(map(int, s.split()))

#     for element in s:
#         heapq.heappush(max_queue, element)
#         heapq.heappush(min_queue, -element)

#     answer = str(max_queue[0]) + ' ' + str(-min_queue[0])
#     return answer