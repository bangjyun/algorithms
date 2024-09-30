from collections import deque

N,M,K=4,4,3
arr = [[6,8,0,1],[0,0,0,0],[0,0,0,0],[0,0,8,0]]


# 배열 변수 2개 사용
def bfs(wi, wj, si, sj):
    visited = [[False] * M for _ in range(N)]
    parent = [[None] * M for _ in range(N)]  # 각 노드의 부모 노드를 저장 => 경로를 위한 변수
    visited[wi][wj] = True
    q = deque()
    q.append((wi, wj))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # BFS로 탐색 시작
    while q:
        i, j = q.popleft()

        ### 목적지에 도달하면 경로변수에 담기 시작
        if (i, j) == (si, sj):  # 목표 지점에 도달하면 경로를 역추적 -> 가장 먼저 도착한 게 최단 경로인 BFS
            path = []
            while (i, j) is not None: # 맨 처음 시작 노드는 부모노드가 없으므로 종료
                path.append((i, j))  # 현재 좌표를 경로에 추가
                if parent[i][j] is None:
                    break  # 부모가 없으면 종료
                i, j = parent[i][j]  # 부모 노드로 이동
            return path[::-1]  # 경로를 반전시켜 올바른 순서로 반환

        for di, dj in directions:
            ni, nj = i + di, j + dj

            # 경계 처리
            # 조건 처리
            if arr[ni][nj] <= 0:
                continue

            # 방문하지 않은 노드에 대해 탐색
            if not visited[ni][nj]:
                visited[ni][nj] = True
                parent[ni][nj] = (i, j)  # 부모 노드를 현재 노드로 저장
                q.append((ni, nj))

    return False  # 경로가 없을 경우
#######################

def bfs(si,sj,ei,ej):
    q = deque()
    v = [[[] for _ in range(M)] for _ in range(N)]  # 경로를 표시하기 위한 visited -> visited 배열에 True 대신 그 부모 노드를 기입

    q.append((si,sj))
    v[si][sj]=(si,sj)
    d = arr[si][sj]             # demage

    while q:
        ci,cj = q.popleft()
        if (ci,cj)==(ei,ej):            # 목적지 좌표 도달
            arr[ei][ej]=max(0, arr[ei][ej]-d)   # 목표 d만큼 타격
            while True:
                ci,cj = v[ci][cj]       # 직전좌표
                if (ci,cj)==(si,sj):    # 시작(공격자)까지 되집어 왔으면 종료
                    return True
                arr[ci][cj]=max(0,arr[ci][cj]-d//2)
                fset.add((ci,cj))

        # 우선순위: 우/하/좌/상 (미방문, 조건: >0 포탑 있고)
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci+di)%N, (cj+dj)%M    # 반대편으로 연결
            if len(v[ni][nj])==0 and arr[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=(ci,cj)
    # 목적지 찾지 못함!!!
    return False