def solution(a, b):
    ab = int(str(a) + str(b))
    op = 2 * int(a) * int(b)
    answer = max(ab, op)
    return answer


a = 91
b = 2
print(solution(a, b))
