from collections import deque

N,M,K=4,4,3
arr = [[6,8,0,1],[0,0,0,0],[0,0,0,0],[0,0,8,0]]
turn = [[0] * M for _ in range(N)]  # 공격한 턴수를 기록(최근공격 체크)

# 최단 경로 찾는 BFS
def bfs(si,sj,ei,ej):
    q=deque()
    q.append((si,sj))
    v=[[]*N for _ in range(M)]
    v[si][sj]=(si,sj)
    d=arr[si][sj]

    while q:
        ci,cj = q.popleft()
        if (ci,cj)==(ei,ej):
            arr[ei][ej]=max(0,arr[ei][ej]-d)
            while True:
                ci,cj=v[ci][cj]
                if (ci,cj)==(si,sj):
                    return True # 목적지 찾음
                arr[cj][cj]=max(0,arr[ci][cj]-d//2)
                fset.add((ci,cj))

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = (ci + di) % N, (cj + dj) % M  # 반대편으로 연결

            if len(v[ni][nj])==0 and arr[ni][nj]>0:
                v[ni][nj]=(ci,cj)
                q.append((ni,nj))

    return False

def bomb(si,sj,ei,ej): # 포탄
    d=arr[si][sj]
    arr[ei][ej]= max(0, arr[ei][ej]-d)

    for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        ni,nj=ei+di,ej+dj
        ni,nj = ni%N, nj%M

        if (ni,nj)!=(si,sj):
            arr[ni][nj] =max(0,arr[ni][nj]-d//2)
            fset.add((ni,nj))


for T in range(1, K + 1):
    # [1] 공격자 선정
    mn, mx_turn,si,sj=5001,0,-1,-1
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0: continue
            if mn>arr[i][j] or (mn==arr[i][j] and mx_turn<turn[i][j]) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and si+sj<i+j) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and si + sj == i + j and sj<j):
                mn, mx_turn,si,sj= arr[i][j],turn[i][j],i,j


    # [2] 공격 대상 선정
    mx, mx_turn, ei, ej = 0, T, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0: continue
            if mx < arr[i][j] or (mx == arr[i][j] and mx_turn > turn[i][j]) or \
                    (mx == arr[i][j] and mx_turn == turn[i][j] and ei + ej > i + j) or \
                    (mx == arr[i][j] and mx_turn == turn[i][j] and ei + ej == i + j and ej > j):
                mx, mx_turn, ei, ej = arr[i][j], turn[i][j], i, j

    # 2-2 레이저 공격
    arr[si][sj]+=(M+N)
    turn[si][sj]=T
    fset=set() # 공격에 참여한 포탑들을 담는 변수
    fset.add((si,sj))
    fset.add((ei, ej))
    if bfs(si,sj,ei,ej)==False:
        # 2-3 포탄 공격
        bomb(si,sj,ei,ej)


    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and (i,j) not in fset:
                arr[i][j]+=1

    cnt = N*M
    for lst in arr:
        cnt-=lst.count(0) # -> 전체 완탐 말고 리스트 단위로 받아서 0 있는지 파악

    if cnt<=1:
        break

    print(max(map(max,arr)))


