def solution(players, callings):
    answer = []
    index_map={value:index for index,value in enumerate(players)}
    for c in callings:
        idx=index_map[c]
        tmp=players[idx] # 순서 변경
        players[idx]=players[idx-1]
        players[idx-1]=tmp
        index_map[c]=idx-1 # 인덱스 변경 반영
        index_map[players[idx]]=idx
    answer=players
    return answer


### 완전 깔끔한 다른사람 코드
def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players