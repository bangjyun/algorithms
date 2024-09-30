def solution(keymap, targets):
    answer = []
    # ["ABCD","AABB"]
    for t in targets:  # "ABCD"
        push = 0
        for Alphabet in t:  # A
            # key =["ABACD", "BCEFD"]
            mn = 101
            for k in keymap:  # "ABACD"
                a = k.find(Alphabet)
                if a == -1:
                    continue
                if mn > a + 1:
                    mn = a + 1
            if mn == 101:
                push = -1
                break
            else:
                push += mn
        answer.append(push)

    return answer
