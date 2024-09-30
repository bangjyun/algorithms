##TODO
## 동시에 => 동시적 상황에서 말 하나, 혹은 맵의 변화가 동시점의 다른 말의 변화에
## 영향을 미치는지 확인하자

from collections import deque

# N,M = map(int,input().split())
# arr=[]
# for i in range(N):
#     arr.append(list(map(int,input().split())))

### TC99
N,M=7,3
arr=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
goal=[[-1,-1]]*(M+1) # 편의점 좌표
goal[1]=[3,1]
goal[2]=[3,3]
goal[3]=[4,2]

### TC5
N,M=4,5
arr = [[1,0,1,1],[1,0,1,1],[0,0,0,1],[1,0,1,1]]
goal=[[-1,-1]]*(M+1) # 편의점 좌표
goal[1]=[3,1]
goal[2]=[2,0]
goal[3]=[2,2]
goal[4]=[2,1]
goal[5]=[0,1]


# goal=[[-1,-1]]*(M+1) # 편의점 좌표
# for i in range(1,M+1):
#     goal[i]=list(map(lambda x:int(x)-1,input().split()))


man=[[-1,-1]]*(M+1)
is_stop=[False]*(M+1)


def in_range(i,j):
    return 0<=i<N and 0<=j<N

def find(si,sj,dests):  # 시작좌표에서 목적지좌표들(set)중 최단거리 동일반경 리스트를 모두 찾기!
    q = deque()
    v = [[0]*(N+2) for _ in range(N+2)]
    tlst = []

    q.append((si,sj))
    v[si][sj]=1

    while q:
        # 동일 범위(반경)까지 처리
        nq = deque()
        for ci,cj in q:
            if (ci,cj) in dests:    # 목적지 찾음! => 더 뻗어나갈 필요없음
                tlst.append((ci,cj))
            else:
                # 네방향, 미방문, 조건: 벽이 아니면 arr[][]==0
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=ci+di, cj+dj
                    if v[ni][nj]==0 and arr[ni][nj]>=0:
                        nq.append((ni,nj))
                        v[ni][nj]=v[ci][cj]+1
        # 목적지 찾았다면(여러개 일수도..) 리턴
        if len(tlst)>0:
            tlst.sort()             # 행/열 오름차순
            return tlst[0]
        q = nq
    # 이곳에 올리는 없지만....
    return -1

def go_to_nextstep(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    # v = [[] * N for _ in range(N)]
    v = [[[] for _ in range(N)] for _ in range(N)] ##
    v[si][sj]=(si,sj)
    path=[]
    while q:
        ci,cj=q.popleft()
        if (ci,cj)==(ei,ej):
            if v[ci][cj] == (si, sj): # 편의점 바로 전 ##TODO
                return ei,ej

            while True:
                path.append((ci, cj))
                ci,cj=v[ci][cj]
                if (ci,cj)==(si,sj):
                    i,j=path[::-1][0]
                    return i,j


        for di,dj in (-1,0),(0,-1),(0,1),(1,0): # 상좌우하
            ni,nj=ci+di,cj+dj
            if in_range(ni, nj) and arr[ni][nj] >= 0 and len(v[ni][nj])==0:
                q.append((ni, nj))
                v[ni][nj] = (ci,cj)

    return -1,-1



def find_basecamp(si,sj):
    q=deque()
    q.append((si,sj))
    visited=[[False]*N for _ in range(N)]
    visited[si][sj] = True ##
    while q:
        ci,cj=q.popleft()
        for di,dj in (-1,0),(0,-1),(0,1),(1,0): # 행 작고 열 작게
            ni,nj=ci+di,cj+dj
            if in_range(ni,nj) and arr[ni][nj]>=0 and visited[ni][nj]==False:
                if arr[ni][nj]==1: # 베캠
                    return ni,nj
                q.append((ni,nj))
                visited[ni][nj]=True

    return False


t=1
while True:
    ns= []
    if t==6:
        s=1
    for m in range(1,M+1):
        if is_stop[m]:
            continue
        if m<t:
            # 1번 행동 bfs 적용해 편의점 최단 경로쪽 한칸 이동 -> 상,좌,우,하
            gi, gj = goal[m]
            si,sj=man[m]

            ni,nj = go_to_nextstep(si,sj,gi,gj)
            man[m] = (ni,nj) # 이동
            # 2번 행동 : 편의점 도착하면 is_stop
            if (gi,gj)==(ni,nj):
                is_stop[m]=True
                ns.append((ni,nj))
                # arr[ni][nj] = -1
            ##TODO: 절대 동시에 움직이는 문제는 개별로 말을 움직이지 X -> 같은 턴 다음 말에 영향을 준다

        elif m==t:
            gi,gj=goal[m]
            # 가까운 베캠 찾기 (bfs) -> 행작은, 열작은
            ni,nj  = find_basecamp(gi, gj)

            # 베이스캠프로 이동 후 -1처리로 칸 블록
            man[m]=(ni,nj)
            ns.append((ni,nj))
            # arr[ni][nj] = -1
#
    for ni,nj in ns:
        arr[ni][nj] = -1

    if is_stop.count(True)==M:
        print(t)
        break
    t += 1
