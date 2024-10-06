a = -4
b = 7
flag = True


def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b


print(solution(a, b, flag))


# 다른 사람의 풀이
def soulution(a, b, flag):
    return a + b if flag else a - b
