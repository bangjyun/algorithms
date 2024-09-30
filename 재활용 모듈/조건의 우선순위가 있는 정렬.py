N,M,K=4,4,3
arr = [[6,8,0,1],[0,0,0,0],[0,0,0,0],[0,0,8,0]]

attack_turn=[[0]*M for _ in range(N)]

## 비교를 하는 최솟값과, 해당 최솟값일 때의 상태들 저장하는 변수 2개 선언
mn = 0
mn_pot = []

### [1] 최댓값이 동일한 원소들을 저장한 배열 생성 -> 같으면 추가하고, 더 크면 배열을 해당 원소로 초기화 ->이전에 쌓이고 있던 건 없어지는 것(최대가 아니니까)
for i in range(N):
    for j in range(M):
        if arr[i][j]<=0:
            continue
        if mn < arr[i][j]: # 초기화
            mn = arr[i][j]
            mn_pot = [(i, j, attack_turn[i][j])]  # 행, 열, 최근 공격 turn
        elif mn == arr[i][j]:
            mn_pot.append((i, j, attack_turn[i][j]))


### [2] 오름차순 정렬// key의 순서대로 -> 같으면 그 다음 키 기준 정렬 //  t[2]가 작은 순 -> 같으면? (t[0] + t[1])가 작은 순 -> 같으면? t[1]가 작은 순
mn_pot.sort(key=lambda t: (t[2], (t[0] + t[1]), t[1]))

# 가장 조건에 맞는 작은 원소의 좌표
si,sj= mn_pot[0][0],mn_pot[0][1]


### [3] 내림차순 정렬 // 부호만 바꿔주면 됨
mn_pot.sort(key=lambda t:(-t[2],-(t[0]+t[1]),-t[1]))


