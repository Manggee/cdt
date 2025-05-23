arr = [5, 1, 4]

def solution(arr):
    x = []
    for i in arr:
        #x += [i] * i
        x.extend([i] * i)
    return x

print(solution(arr))