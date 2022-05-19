# https://www.acmicpc.net/problem/4796



# 8일중 1일, 
# P * N > 20 일 때, N-1이 정답




# page = 0
# while(True):
#     l, p, v = list(map(int, input().split()))
#     page +=1 
#     if l+p+v==0:
#         break 
    
#     duration = v//p*l
#     # remaining = v%p if l >= v%p else l
#     remaining = min(v%p, l)
#     result = (duration) + remaining
#     print(f"Case {page}: {result}")
        
        
# import sys
# input = sys.stdin.readline

# i = 1
# while True:
#     l, p, v = map(int, input().split())
#     if l+p+v == 0:
#         break
#     res = (v//p)*l
#     res += min((v%p), l)
#     print('Case %d: %d' %(i, res))
#     i += 1