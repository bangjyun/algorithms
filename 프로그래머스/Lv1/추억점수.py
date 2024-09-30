def solution(name, yearning, photo):
    answer = []
    index_map={k:v for k,v in zip(name,yearning)}
    for p in photo:
        tot=0
        for person in p:
            tot+=index_map.get(person,0)
        answer.append(tot)
    return answer