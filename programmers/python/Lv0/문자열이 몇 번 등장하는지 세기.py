myString = "aaaa"
pat = "aa"

def solution(myString, pat):
    count = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i : i+len(pat)] == pat:
            count += 1
    return count
print(solution(myString, pat))

# 사실 끝에서 pat 길이만큼 남을 때까지만 탐색을 하는 것이 맞다. 근데 지식 부족으로 인해 구현하지 못하고 참고했다.