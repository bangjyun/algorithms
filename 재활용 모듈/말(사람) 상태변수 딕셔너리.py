N, M, K = map(int, input().split())

## TODO: 2차원 빈리스트
arr = [list(map(int, input().split())) for _ in range(N)] #-> 그냥 2차원 배열 (맵)
gun = [[[] for _ in range(N)] for _ in range(N)]

### TODO: 2차원 빈리스트 안에 리스트 -> 3차원
for i in range(N):
    for j in range(N):
        if arr[i][j]>0:
            gun[i][j].append(arr[i][j])

arr = [[0]*N for _ in range(N)]

## TODO: 사람 객체 -> 상태 변수 (구조체 느낌) => 딕셔너리
# [0]:i, [1]:j, [2]:dir, [3]:power,[4]:gun,[5]:score  방향 0,1,2,3 (↑, →, ↓, ←)
players = {}            # 1~M 플레이어
for m in range(1,M+1):
    i,j,d,p = map(int, input().split())
    players[m]=[i-1,j-1,d,p,0,0]
    arr[i-1][j-1]=m

# 반대 방향 opp[0]=2, opp[2]=0 -> key:value로 dictionary로
opp = {0:2, 1:3, 2:0, 3:1}
