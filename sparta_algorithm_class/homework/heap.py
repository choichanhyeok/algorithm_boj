import heapq


# def solution(s):
#     arr = list(map(int, s.split(' ')))
#     return str(min(arr)) + " " + str(max(arr))

def solution(s):
    max_queue = []
    s = s.split()
    for element in s:
        heapq.heappush(max_queue, int(element))

    answer = str(max_queue[0]) + ' ' + str(max_queue[-1])
    return answer


print(solution("-1 -2 -3 -4 -5"))
solution("1 2 3 4")