# 10*10 격자, 100턴 (10명 이동, 회전, 값 감소 처리): 시간 충분!
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

si,sj,L = find_square(arr)  # 좌상단 좌표 반환

narr = [x[:] for x in arr]
for i in range(L):
    for j in range(L):
        narr[si+i][sj+j]=arr[si+L-1-j][sj+i]

        if narr[si+i][sj+j]>0:      # 벽이면 회전시 1감소 -> 문제 상 조건
            narr[si+i][sj+j]-=1