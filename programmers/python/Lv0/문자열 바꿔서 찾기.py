myString = "ABBAA"
pat = "AABB"

def solution(myString, pat):
    target = []
    for i in myString:
        if i == "A":
            target.append("B")
        else:
            target.append("A")
    target = ''.join(target)
    if pat in target:
        return 1
    else:
        return 0
print(solution(myString, pat))


# join 함수
# '구붖자'.join(list)
