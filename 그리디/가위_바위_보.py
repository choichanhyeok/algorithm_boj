# 가위 바위 보는 두 사람이 즐기는 유명한 게임이다. 각 플레이어는 자신의 손을 이용해서 가위, 바위, 보 중 한 모양을 만들어야 한다. 두 플레이어가 같은 모양을 만든 경우에는 비기게 된다. 가위는 보를 이기고, 보는 바위, 바위는 가위를 이긴다.
# 상근이는 사람들의 심리를 수십년동안 연구한 결과 가위 바위 보를 한국에서 가장 잘 하는 사람이 되었다. 상근이는 일대일 가위 바위 보를 절대로 지지 않는다.
# 한국에 적수가 없다고 판단한 상근이는 세계 대회에 나가기로 했다. 요즘 상근이는 세계 대회를 대비해 훈련중이다. 훈련은 친구 N명과 동시에 한다. 가위바위보는 총 R개의 라운드로 이루어져 있고, 각 라운드마다 상근이와 친구들은 세 모양중 하나를 만들어야 한다.
# 각 라운드의 점수 계산은 상근이와 친구 개개인을 독립적으로 비교한다. 상근이가 이기면 2점, 비기면 1점, 지면 0점이다.
# 상근이와 친구들이 각 라운드에 낸 모양이 주어졌을 때, 게임이 끝나고 난 후 상근이의 점수를 구한다. 그 다음, 상근이가 친구들이 무엇을 낼지 미리 알고있었다고 가정할 때, 상근이가 얻을 수 있는 최고 점수를 구하는 프로그램을 작성하시오.



# 입력 1: 라운드 수 R
# 입력 2: 각 라운드에 낸 모양(S: 가위, P: 보, R: 바위)
# 입력 3: 친구의 수 N
# 입력 4: 상근이의 친구들이 각 라운드에 낸 모양, 한 사람당 한 라인씩
# ....

# 인풋 정리
# 입력 4부터, 친구의 수 만큼 반복해서 가위바위보 패턴을 입력 받는다.


Round = int(input())
Sangeon_pattern = input()
n = int(input())

sangeon_score = 0
dream_score = 0

for i in range(n):
    enemy_pattern = input()
    for j in range(Round):
        dream_score += 2
        if enemy_pattern[j] == Sangeon_pattern[j]:
            sangeon_score += 1
        elif enemy_pattern[j] == 'P' and Sangeon_pattern[j] == 'S':
            sangeon_score += 2
        elif enemy_pattern[j] == 'R' and Sangeon_pattern[j] == 'P':
            sangeon_score += 2
        elif enemy_pattern[j] == 'S' and Sangeon_pattern[j] == 'R':
            sangeon_score += 2

print(sangeon_score)
print(Round*2*n)







