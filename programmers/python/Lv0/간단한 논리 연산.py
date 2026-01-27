def solution(x1, x2, x3, x4):
    answer = (x1 and x2) or (x3 and x4)
    return answer


x1 = True
x2 = False
x3 = False
x4 = False

print(solution(x1, x2, x3, x4))

