n = 10
num = []

def solution(n):
    answer = 0
    if n%2 == 0:
        for arr in range(1, n + 1):
            if arr % 2 == 0:
                num.append(arr)
                answer += arr*arr
            else:
                continue
    else:
        for arr in range(1, n + 1):
            if arr % 2 == 1:
                num.append(arr)
                answer += arr
            else:
                continue

            
    return answer
print(solution(n))