numbers = [58, 44, 27, 10, 100]
n = 139

def solution(numbers, n):
    result = 0
    for num in numbers:
        result += num
        if result > n:
            return result
    return result
print(solution(numbers, n))