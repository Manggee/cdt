included = [True, False, False, True, True]
a = 3
d = 4


def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer


print(solution(a, d, included))
