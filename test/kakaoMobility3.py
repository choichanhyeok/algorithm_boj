from collections import deque

def solution(s, times):
    answer = []
    time_limit_dict = {0: 99, 1: 23, 2: 59, 3: 59}

    start_time = s.split(':')[2:]
    now_time = start_time
    times = deque(times)

    how_long = 0
    continuous_array = []

    # (0) s에 times의 원소들을 더해주는 걸 먼저 구해보자!!!!!!!!
    while times:
        time = times.popleft().split(':')

        for i in range(len(now_time)):
            element_sum = now_time[i] + time[i] # 현재시간 + 더해줄 시간

            if i == 0:                # (1) date의 경우
                if 30 < element_sum:
                    now_time[i] = 1     # 1일로 변경
                    how_long += element_sum
                    continuous_array.append(now_time[i])
                else:
                    now_time[i] += element_sum
                    how_long += element_sum
                    continuous_array.append(now_time[i])
            elif i == 1:              # (2) 시간의 경우
                if 23 < element_sum:
                    now_time[i-1] += 1
                    how_long += 1
                    continuous_array.append(now_time[i-1]+1)
                else:
                    now_time[i] = element_sum
            elif i == 2:            # (3) 분의 경우
                if 59 < element_sum:
                    now_time[i-1] += 1
                    continuous_array.append(now_time[i - 1] + 1)
                else:
                    now_time[i] = element_sum
            elif i == 3:
                if 59 < element_sum:
                    now_time[i-1] += 1
                else:
                    now_time[i] = element_sum




            print(now_time[i])
            print(time[i])


        print(time)

    # (1) s에 times를 누적해서 더해주며, '일'이 넘을때 리턴할 date를.
    # (2) s에 times를 누적해서 더해주며, 만약 '일'이 연속적이지 않은 경우 실패(0) 리턴, +성공은 (1) 리턴

    return answer


solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"])