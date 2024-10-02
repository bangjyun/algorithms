## TODO 1 : gap을 변수로 이용한 풀이
def solution(plans):
    answer = []
    arr=[]
    stack=[]
    for p in plans:
        h=int(p[1][:2])
        m=int(p[1][3:5])
        ntime=h*60+m
        arr.append([p[0],ntime,int(p[2])])
    arr.sort(key= lambda x:x[1])

    for i in range(len(arr)-1):
        t1,t2=arr[i][1],arr[i+1][1]
        gap=t2-t1
        stack.append([arr[i][0],arr[i][2]]) # 이름, 남은 시간
        if gap>0:
            while stack and gap:
                if gap>=stack[-1][1]:
                    s=stack.pop()
                    answer.append(s[0])
                    gap-=s[1]
                else: # 남지 않으면
                    stack[-1][1]-=gap
                    gap=0
        else:
            s=stack.pop()
            answer.append(s[0])
    answer.append(arr[-1][0])
    for s in stack[::-1]:
        answer.append(s[0])
    return answer

# TODO 2:  #=> 이새끼 이해 안 됨
def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()
    print(list(map(lambda x: x[1], lst)))
    return list(map(lambda x: x[1], lst))
plans=[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
solution(plans)