number = 55
n = 10
m = 5


def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0


print(solution(number, n, m))
