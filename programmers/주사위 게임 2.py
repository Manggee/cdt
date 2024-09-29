a = 4
b = 4
c = 4


# def solution(a, b, c):
#     answer = 0

#     result = a + b + c
#     result2 = a**2 + b**2 + c**2
#     result3 = a**3 + b**3 + c**3

#     if a != b != c != a:
#         answer = result
#     elif a == b == c:
#         answer = (result) * (result2) * (result3)
#     else:
#         answer = (result) * (result2)
#     return answer


# print(solution(a, b, c))


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


print(solution(a, b, c))
