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
                    if v[ni][nj]==0 and arr[ni][nj]==0:
                        nq.append((ni,nj))
                        v[ni][nj]=v[ci][cj]+1
        # 목적지 찾았다면(여러개 일수도..) 리턴
        if len(tlst)>0:
            tlst.sort()             # 행/열 오름차순
            return tlst[0]
        q = nq
    # 이곳에 올리는 없지만....
    return -1
