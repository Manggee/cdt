included = [True, False, False, True, True]
a = 3
d = 4


def solution(a, d, included):
    answer = 0
    for i in included:
        if i == True:
            answer.append(i)
        return answer


print(solution(a, d, included))
