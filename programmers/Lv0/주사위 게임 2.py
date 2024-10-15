a = 4
b = 4
c = 4


# 내가 생각한 답변
def solution(a, b, c):
    answer = 0
    if a == b and b == c:
        answer = (
            (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c)
        )
    elif a == b or a == c or b == c:
        answer = (a + b + c) * (a * a + b * b + c * c)
    else:
        answer = a + b + c

    return answer


# 처음에 틀린이유
# a == b or b == c or a == c 라는 조건에는 a,b,c가 동일한 경우도 포함된다.
# 저 조건을 제일 먼저 작성했기에 a,b,c가 전부 동일한 경우로 계산되지 않고 상위에서 이미 계산이 끝나버렸다.

print(solution(a, b, c))


# 다른 사람의 풀이
def solution(a, b, c):
    answer = 0

    result = a + b + c
    result2 = a**2 + b**2 + c**2
    result3 = a**3 + b**3 + c**3

    if a != b != c != a:
        answer = result
    elif a == b == c:
        answer = (result) * (result2) * (result3)
    else:
        answer = (result) * (result2)
    return answer


print(solution(a, b, c))
