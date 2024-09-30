from collections import deque

# N, M, K= map(int,input().split())
# arr=[]
# for _ in range(N):
#     arr.append(list(map(int,input().split())))
# TC1
N,M,K=4,4,2
arr = [[0,1,4,4],[8,0,10,13],[8,0,11,26],[0,0,0,0]]

attack_turn=[[0]*M for _ in range(N)]

def weakest():
    mn=5000
    mn_pot=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:
                continue
            if mn>arr[i][j]:
                mn=arr[i][j]
                mn_pot=[(i,j,attack_turn[i][j])] # 행, 열, 최근 공격 turn
            elif mn==arr[i][j]:
                mn_pot.append((i,j,attack_turn[i][j]))

    mn_pot.sort(key=lambda t:(-t[2],-(t[0]+t[1]),-t[1]))

    wi, wj =mn_pot[0][0],mn_pot[0][1]
    arr[wi][wj]+=(N+M)
    return wi,wj,arr[wi][wj]

def strongest():
    mn = 0
    mn_pot = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:
                continue
            if mn < arr[i][j]:
                mn = arr[i][j]
                mn_pot = [(i, j, attack_turn[i][j])]  # 행, 열, 최근 공격 turn
            elif mn == arr[i][j]:
                mn_pot.append((i, j, attack_turn[i][j]))

    mn_pot.sort(key=lambda t: (t[2], (t[0] + t[1]), t[1]))
    si,sj= mn_pot[0][0],mn_pot[0][1]

    return si,sj


def bfs(wi, wj, si, sj):
    visited = [[False] * M for _ in range(N)]
    parent = [[None] * M for _ in range(N)]  # 각 노드의 부모 노드를 저장
    visited[wi][wj] = True
    q = deque()
    q.append((wi, wj))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # BFS로 탐색 시작
    while q:
        i, j = q.popleft()

        if (i, j) == (si, sj):  # 목표 지점에 도달하면 경로를 역추적
            path = []
            while (i, j) is not None:
                path.append((i, j))  # 현재 좌표를 경로에 추가
                if parent[i][j] is None:
                    break  # 부모가 없으면 종료
                i, j = parent[i][j]  # 부모 노드로 이동
            return path[::-1]  # 경로를 반전시켜 올바른 순서로 반환

        for di, dj in directions:
            ni, nj = i + di, j + dj

            ###### 격자 밖을 벗어나면 반대쪽으로 -> moduler 연산  ex -1%4=3, 5%4=1 -> 격자가 0,1,2,3일 때 크기가 4면 일케 됨
            ni = ni%N
            nj = nj%M

            # 공격력 0 이하인 곳은 건너뜀
            if arr[ni][nj] <= 0:
                continue

            # 방문하지 않은 노드에 대해 탐색
            if not visited[ni][nj]:
                visited[ni][nj] = True
                parent[ni][nj] = (i, j)  # 부모 노드를 현재 노드로 저장
                q.append((ni, nj))

    return False  # 경로가 없을 경우


for turn in range(1,K+1):
    attacked = [[False] * M for _ in range(N)]
    # 대상자 선정
    si, sj = strongest()
    # 공격자 선정
    wi,wj,pwr=weakest()

    # 공격
    trace=bfs(wi,wj,si,sj)
    attack_turn[wi][wj] = turn
    attacked[wi][wj]=True

    if trace is not False:
        ## 레이저 공격
        for i,j in trace[1:-1]:
            if arr[i][j] >0:
                arr[i][j] -= pwr // 2
                attacked[i][j] = True

        arr[si][sj]-=pwr
        attacked[si][sj] = True

    else:
        ## 포탄 공격
        arr[si][sj]-=pwr
        attacked[si][sj] = True
        for di,dj in (1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1):
            ni,nj = si-di,sj-dj

            ni = ni % N
            nj = nj % M

            if arr[ni][nj]<=0 or (ni, nj) == (wi, wj):
                continue
            arr[ni][nj]-=pwr//2 # 주변
            attacked[ni][nj] = True # 공격 당한 turn


    # 공격과 무관 포탑 +1
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:
                continue
            if attacked[i][j]== True:
                continue
            else:
                arr[i][j]+=1

    # 종료 조건
    cnt=N*M
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:
                cnt-=1
    if cnt <=1:
        break

print(max(map(max,arr)))  # 2차원 배열 최댓값 출력
# si,sj=strongest()
# print(arr[si][sj])